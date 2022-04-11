from importlib.util import set_loader
from typing import List
from fastapi import WebSocket
import websockets

class Notifier:
    def __init__(self):
        self.connection :List = []
        self.no_of_player = 0
        self.grid  = [[0 for i in range(3)]
                      for j in range(3)]
        
    async def connect(self,websocket:WebSocket,username:str,game:int):
        await websocket.accept()
        self.connection.append([websocket,username,game])
    def disconnet(self,websocket:WebSocket,username:str,game:int):
        index = self.connection.index([websocket,username,game])
        self.connection.pop(index)
    
    async def send_personal_message(self, message: str, websocket: WebSocket,username:str):
        await websocket.send_text(message)

    async def broadcast(self, message:str,game:int):
        for player in self.connection:
            if(player[2] == game):
                await player[0].send_text(message)
    async def broadcast_result(self,message):
        for player in self.connection:
            await player[0].send_text(message)
            
            
    async def game(self,row,col,move):
        if (self.grid[row][col]==0):
            self.grid[row][col] = move
        return self.grid
    
    async def result(self):
        winner = ''
        if(self.grid[0][0] == 'X' and self.grid[0][1] == 'X' and self.grid[0][2] == 'X'):
            winner = 'X'
        if(self.grid[1][0] == 'X' and self.grid[1][1] == 'X' and self.grid[1][2] == 'X'):
            winner = 'X'
        if(self.grid[2][0] == 'X' and self.grid[2][1] == 'X' and self.grid[2][2] == 'X'):
            winner = 'X'
        if(self.grid[0][0] == 'X' and self.grid[1][0] == 'X' and self.grid[2][0] == 'X'):
            winner ='X'
        if(self.grid[0][1] == 'X' and self.grid[1][1] == 'X' and self.grid[2][1] == 'X'):
            winner = 'X'
        if(self.grid[0][2] == 'X' and self.grid[1][2] == 'X' and self.grid[2][2] == 'X'):
            winner = 'X'
        if(self.grid[0][0] == 'X' and self.grid[1][1] == 'X' and self.grid[2][2] == 'X'):
            winner = 'X'
        if(self.grid[0][2] == 'X' and self.grid[1][1] == 'X' and self.grid[2][0] == 'X'):
            winner = 'X'
        
        if(self.grid[0][0] == 'O' and self.grid[0][1] == 'O' and self.grid[0][2] == 'O'):
            winner = 'O'
        if(self.grid[1][0] == 'O' and self.grid[1][1] == 'O' and self.grid[1][2] == 'O'):
            winner = 'O'
        if(self.grid[2][0] == 'O' and self.grid[2][1] == 'O' and self.grid[2][2] == 'O'):
            winner = 'O'
        if(self.grid[0][0] == 'O' and self.grid[1][0] == 'O' and self.grid[2][0] == 'O'):
            winner ='O'
        if(self.grid[0][1] == 'O' and self.grid[1][1] == 'O' and self.grid[2][1] == 'O'):
            winner = 'O'
        if(self.grid[0][2] == 'O' and self.grid[1][2] == 'O' and self.grid[2][2] == 'O'):
            winner = 'O'
        if(self.grid[0][0] == 'O' and self.grid[1][1] == 'O' and self.grid[2][2] == 'O'):
            winner = 'O'
        if(self.grid[0][2] == 'O' and self.grid[1][1] == 'O' and self.grid[2][0] == 'O'):
            winner = 'O'
        print(winner)
        count = 0;
        for i in self.grid:
            for j in i:
                if(j !=0):
                    count+=1
        
        if(winner == 'X' or winner == 'O'):
            return {"message":winner+" Won the game!!"}
        elif winner == '' and count == 9 :
            return {"message":"Draw"}
        
        
            
            
        
        
        