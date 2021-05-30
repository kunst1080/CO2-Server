import asyncio
import websockets
import os

address = os.getenv("WS_HOST", "127.0.0.1")
port = os.getenv("WS_PORT", "1111")

async def hello():
    uri = f"ws://{address}:{port}"
    async with websockets.connect(uri) as websocket:
        r = await websocket.recv()
        print(r)
        r = await websocket.recv()
        print(r)

asyncio.get_event_loop().run_until_complete(hello())

print("Finish.")
