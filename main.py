import asyncio
import websockets
import json
import os

from CO2Meter import *

address = os.getenv("WS_HOST", "127.0.0.1")
port = os.getenv("WS_PORT", "1111")
interval = int(os.getenv("INTERVAL", 2))

sensor = CO2Meter("/dev/hidraw0")

async def server(websocket, path):
    print(f"connection start: {path}")
    try:
        while True:
            await asyncio.sleep(interval)
            data = sensor.get_data()
            s = json.dumps(data)
            await websocket.send(s)
    except websockets.ConnectionClosed:
        print("closed")
        await websocket.close()

start_server = websockets.serve(server, address, port)
print(f"start srver - {address}:{port}")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
