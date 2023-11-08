from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials  
from enum import Enum

app = FastAPI()

security = HTTPBearer()


class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"


# 模拟数据库存储资源数据
# 权限资源
permissions = {
    "admin": ["read", "write", "delete"],
    "user": ["read"]
}

# 对象操作资源
object_operations = {
    "read": ["article", "comment"],
    "write": ["article", "comment"],
    "delete": ["article"]
}


def get_user_role(username: str) -> Role:
    # 假设从数据库中获取用户角色
    return Role.ADMIN if username == "admin" else Role.USER


def has_permission(user_role: Role, required_permission: str) -> bool:
    user_permissions = permissions.get(user_role.value)
    return required_permission in user_permissions if user_permissions else False


def has_object_operation(user_role: Role, required_operation: str, object_type: str) -> bool:
    allowed_operations = object_operations.get(required_operation)
    return object_type in allowed_operations if allowed_operations else False


def check_permission(required_permission: str, 
                    object_type: str = None,
                    credentials: HTTPAuthorizationCredentials = Depends(security),  
                    username: str = Header(...)):
    
    user_role = get_user_role(username)  
    print(user_role)
    if user_role is None:
         raise HTTPException(status_code=401, detail="Invalid username or role")
    if not has_permission(user_role, required_permission):
        raise HTTPException(status_code=403, detail="Insufficient permissions")
    if object_type and not has_object_operation(user_role, required_permission, object_type):
        raise HTTPException(status_code=403, detail="Object operation not allowed")

@app.get("/articles/{article_id}")
def read_article(article_id: int, 
                credentials: HTTPAuthorizationCredentials = Depends(security),
                username: str = Header(...)):
    check_permission("read", object_type="article", credentials=credentials, username=username)
    return {"message": f"Read article {article_id}"}


@app.post("/articles")
def create_article(credentials: HTTPAuthorizationCredentials = Depends(security),
                username: str = Header(...)):
    check_permission("write", object_type="article", credentials=credentials, username=username)
    return {"message": "Create article"}


@app.delete("/articles/{article_id}")
def delete_article(article_id: int, credentials: HTTPAuthorizationCredentials = Depends(security),
                username: str = Header(...)):
    check_permission("delete", object_type="article", credentials=credentials, username=username)
    return {"message": f"Delete article {article_id}"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, host="0.0.0.0", port=8000)