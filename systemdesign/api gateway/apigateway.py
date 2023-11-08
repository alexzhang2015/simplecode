from pydantic import BaseModel
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, FastAPI, HTTPException, status, Request
from jose import JWTError, jwt
from typing import Deque, Optional
from datetime import timedelta, datetime
from circuitbreaker import circuit
import requests
import time
from collections import deque

app = FastAPI()


class RateLimit:
    def __init__(self, times: int, seconds: int):
        self.times = times
        self.seconds = seconds
        self.clients: Deque = deque()

    def __call__(self, request: Request):
        client_addr = request.client.host
        curr_time = time.time()

        # 清理时间窗口之外的请求记录
        while self.clients and self.clients[0][1] < curr_time - self.seconds:
            self.clients.popleft()

        # 检查是否超过限流阈值
        if len(self.clients) >= self.times:
            raise HTTPException(status_code=429, detail="Too many requests")

        # 添加新的请求记录
        self.clients.append((client_addr, curr_time))

# 限流
@app.get("/", dependencies=[Depends(RateLimit(times=5, seconds=60))])
async def test(request: Request):
    return {"message": "Hello World"}


# 熔断
@circuit(failure_threshold=5, recovery_timeout=30)
@app.get("/users")
async def get_users():
    response = requests.get("http://localhost:8001/users")
    return response.json()

# 降级
@app.get("/orders")
def get_orders():
    try:
        return requests.get("http://localhost:8001/orders").json()
    except:
        return {"data": []}


# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "alex": {
        "username": "alex",
        "full_name": "Alex Smith",
        "email": "alex@example.com",

        # https://www.bejson.com/encrypt/bcrpyt_encode/ 密码：alex
        "hashed_password": "$2a$10$P4OnNXOejmqqWRp8vqi0KuxOUpLv.KzIZ7L.FLJ6Az67k6GZwWcCq",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@app.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(
        fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


# API聚合
@app.get("/products/{product_id}")
async def get_product(product_id: int, user: User = Depends(get_current_user)):
    product_response = requests.get(
        f"http://localhost:8001/products/{product_id}")
    reviews_response = requests.get(
        f"http://localhost:8001/reviews?product_id={product_id}")

    product = product_response.json()
    reviews = reviews_response.json()

    return {**product, "reviews": reviews}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
