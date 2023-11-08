from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

app = FastAPI()

class UserMessage(BaseModel):
    content: str 

# 创建数据库连接
engine = create_engine("sqlite:///messages.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 定义消息模型
class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    content = Column(String)
    is_read = Column(Boolean, default=False)

# 创建数据库表
Base.metadata.create_all(bind=engine)

templates = {
    "template1": "Hello, {name}! You have a new message: {message}",
    "template2": "Hi there, {name}! You received a new notification: {notification}"
}

active_connections = {}

async def send_message(websocket: WebSocket, message: str):
    await websocket.send_text(message)

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(user_id: int, websocket: WebSocket):
    await websocket.accept()
    active_connections[user_id] = websocket
    try:
        while True:
            message = await websocket.receive_text()
            # 模拟从数据库或其他数据源中获取用户的消息模版和消息内容
            template = templates.get("template1")
            name = f"User {user_id}"
            formatted_message = template.format(name=name, message=message)
            
            # 持久化消息到数据库
            db = SessionLocal()
            db_message = Message(user_id=user_id, content=formatted_message)
            db.add(db_message)
            db.commit()
            db.refresh(db_message)
            
            await send_message(websocket, formatted_message)
    except:
        del active_connections[user_id]

@app.get("/get_messages/{user_id}")
async def get_messages(user_id: int):
    websocket = active_connections.get(user_id)
    if websocket is None:
        return {"message": "User not connected"}
    
    # 从数据库中获取用户的未读消息
    db = SessionLocal()
    messages = db.query(Message).filter(Message.user_id == user_id, Message.is_read == False).all()
    
    # 将未读消息设置为已读
    for message in messages:
        message.is_read = True
    db.commit()
    
    message_texts = [message.content for message in messages]
    
    await send_message(websocket, "\n".join(message_texts))
    return {"message": "Messages sent"}

@app.post("/send/{user_id}")
async def send_http_message(user_id: int, message: UserMessage):
    # 模拟从数据库或其他数据源中获取用户的消息模版
    template = templates.get("template2")
    name = f"User {user_id}"
    formatted_message = template.format(name=name, notification=message.content)

    websocket = active_connections.get(user_id)
    if websocket is None:
        return {"message": "User not connected"}
    
    # 持久化消息到数据库
    db = SessionLocal()
    db_message = Message(user_id=user_id, content=formatted_message)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    
    await send_message(websocket, formatted_message)
    return {"message": "Message sent"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
