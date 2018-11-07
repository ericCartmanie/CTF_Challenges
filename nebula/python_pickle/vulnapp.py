import os
import pickle
import time
import socket
import signal

signal.signal(signal.SIGCHLD,signal.SIG_IGN)

def server(my_socket):
    line = my_socket.recv(1024)
    obj = pickle.loads(line)
    for i in obj:
        my_socket.send("why did you send me "+i+"?\n")

my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
my_socket.bind(('0.0.0.0',10013))
my_socket.listen(10)

while True:
    client, addr = my_socket.accept()
    if(os.fork() == 0):
        client.send("Accepted connection from %s:%d" % (addr[0], addr[1]))
        server(client)
        exit(1)
