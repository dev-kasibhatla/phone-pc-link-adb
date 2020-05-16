import sys
import socket, threading
import logging

keepRunning = True

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-9s) %(message)s',)

HOST = '' # Accepting clients from any IP addresses
PORT = 9090

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(4)

clients = [] #list of clients connected
lock = threading.Lock()

commands=[]

class tServer(threading.Thread):
    def __init__(self,tup):        
        threading.Thread.__init__(self)
        #split tuple
        self.socket, self.address = tup

    def run(self):	
        lock.acquire()
        clients.append(self)
        lock.release()
        print ('%s:%s connected.' % self.address)

        while keepRunning:
            #data = self.socket.recv(1024)            
            if len(commands) == 0:
                continue 
            else:
                c = commands.pop()
                self.socket.send((c + "\n").encode())
              
        self.socket.close()
        print ('%s:%s disconnected.' % self.address)
        lock.acquire()
        clients.remove(self)
        lock.release()
        pri("Stopping network")


def init():
    pri('Starting')
    while keepRunning:
        tServer(s.accept()).start()
    pri("Killing")
    t1._stop()

def pri(m):
    logging.debug(m)

t1 = threading.Thread(name="nethread",target=init)
t1.start()