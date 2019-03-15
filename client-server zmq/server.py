"""
saeid ghasemshirazi
94403036
"""

import  zmq


context = zmq.Context()
#zmq.rep for reply client requests
#ZMQ REQ sockets can connect to many servers.
#socket zmq.REQ will block on send unless it has successfully received a reply back.

socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:8877")

while True:
    #socket.recv for recieve msg form client 
    msg = socket.recv()
    print("from client: ",msg)
    server_msg=input("enter your msg here: ")
    socket.send_string(server_msg)
    print("################################")
