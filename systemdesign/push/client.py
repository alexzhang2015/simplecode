import asyncio
import websockets

async def receive_messages(user_id):
    async with websockets.connect(f'ws://localhost:8000/ws/{user_id}') as websocket:
        while True:
            message = await websocket.recv()
            print(f"User {user_id} received message: {message}")

async def simulate_users():
    user_ids = [1, 2, 3]  # 设置要模拟的用户ID列表
    tasks = []
    
    for user_id in user_ids:
        task = asyncio.create_task(receive_messages(user_id))
        tasks.append(task)

    await asyncio.gather(*tasks)

asyncio.get_event_loop().run_until_complete(simulate_users())
