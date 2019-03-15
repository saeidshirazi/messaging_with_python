'''
saeid ghasemshirazi
94403036
'''
import  zmq


#Contexts are thread safe unlike sockets. An application can create and manage multiple contexts.
context = zmq.Context()
#zmq.req for send request to server
#socket zmq.REP will block on recv unless it has received a request.
socket = context.socket(zmq.REQ)
socket.connect("tcp://server_ip:8877")


while True:
    msg=input("Please enter your msg here: ")
    socket.send_string(msg)
    print( 'sending',msg)
    print("from server : ", socket.recv())
