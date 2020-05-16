import sys
import socket, threading

HOST = '' # Accepting clients from any IP addresses
PORT = 9090

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(4)

clients = [] #list of clients connected
lock = threading.Lock()

status = "off"

class chatServer(threading.Thread):
    def __init__(self,tup):        
        threading.Thread.__init__(self)
        #split tuple
        self.socket, self.address = tup

    def run(self):	
        lock.acquire()
        clients.append(self)
        lock.release()
        print ('%s:%s connected.' % self.address)

        while True:
            data = self.socket.recv(1024)
            if not data:
                break
            else:
                data = data.strip()
                print ("received command: " + str(data) + "\n")
              
                val = process_commands(data)
                print("sending reply: " + val + "\n")
                self.socket.send((val + "\n").encode())
              
        self.socket.close()
        print ('%s:%s disconnected.' % self.address)
        lock.acquire()
        clients.remove(self)
        lock.release()

def process_commands(command):
    global status
    if command == "on":
        status = "device on"
        return status
    elif command == "off":
        status = "device off"
        return status
    else: return "?"

while True:
    chatServer(s.accept()).start() # start telnet server