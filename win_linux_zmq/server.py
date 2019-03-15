import  zmq


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://0.0.0.0:8877")

while True:
    msg = socket.recv()
    print("from client: ",msg)
    server_msg=input("enter your msg here: ")
    socket.send_string(server_msg)
    print("")
