import telnetlib 
import json

class Challenge: 
    def __init__(self,PORT,HOST = 'socket.cryptohack.org'): 
        self.tn = telnetlib.Telnet(HOST, PORT)

    def readline(self):
        return self.tn.read_until(b"\n")

    def json_recv(self):
        line = self.readline()
        return json.loads(line.decode())

    def json_send(self, hsh):
        request = json.dumps(hsh).encode()
        self.tn.write(request)