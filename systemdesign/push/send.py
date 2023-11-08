import asyncio
import httpx

async def send_message(user_id, message):
    async with httpx.AsyncClient() as client:
        url = f"http://localhost:8000/send/{user_id}"
        payload = {"content": message}
        await client.post(url, json=payload)

async def simulate_concurrent_messages():
    user_ids = [1, 2, 3]
    message_count = 10
    message = "Hello, WebSocket!"

    tasks = []
    for user_id in user_ids:
        for _ in range(message_count):
            task = asyncio.create_task(send_message(user_id, message))
            tasks.append(task)

    await asyncio.gather(*tasks)

# 运行示例
asyncio.run(simulate_concurrent_messages())