from unittest import result
from fastapi import FastAPI,WebSocket,WebSocketDisconnect
from logic.Notfier import Notifier
import json
import numpy as np


manager = Notifier()
app = FastAPI()

@app.websocket("/ws/{username}/{game}")
async def define_game_endpoint(websocket:WebSocket,username:str,game:int):
    await manager.connect(websocket,username,game)
    try:
        while True:
            data = json.loads(await websocket.receive_text())
            row = data['x']
            col = data['y']
            move = data['move']
            grid = await manager.game(row,col,move)
            print(np.matrix(grid))
            result = json.dumps(await manager.result())
            if result:
                await manager.broadcast_result(result)
    except WebSocketDisconnect:
        manager.disconnet(websocket,username,game)

