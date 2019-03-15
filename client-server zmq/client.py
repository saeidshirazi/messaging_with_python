import  zmq


#Contexts are thread safe unlike sockets. An application can create and manage multiple contexts.
context = zmq.Context()
#zmq.req for send request to server
#socket zmq.REP will block on recv unless it has received a request.
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:8877")


while True:
    msg=input("Please enter your msg here: ")
    socket.send_string(msg)
    print( 'sending',msg)
    print("from server : ", socket.recv())
