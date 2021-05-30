import asyncio
import websockets

async def hello():
    uri = "ws://127.0.0.1:1111"
    async with websockets.connect(uri) as websocket:
        r = await websocket.recv()
        print(r)
        r = await websocket.recv()
        print(r)

asyncio.get_event_loop().run_until_complete(hello())

print("Finish.")
