from pwn import * 
import json

class Challenge: 
    def __init__(self,PORT,HOST = 'socket.cryptohack.org'): 
        self.ch = remote(HOST, PORT)
        context.log_level = 'ERROR'
        self.ch.recv()

    def send(self, m): 
        self.ch.sendline(json.dumps(m).encode())

    def receive(self): 
        return json.loads(self.ch.recvline().decode().strip())