import socket
import threading

port=5050
host=socket.gethostbyname(socket.gethostname())
addr=(host ,port)
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    soc.bind(addr)
except:
    print('an error occured')
else:
    print('binding is successful')    


def userhandler(conn,adr):
    data=soc.recv(1280)
    endata=data.decode('utf-8')
    print(data)


def acceptcon():
    while True:
        soc.listen(1)
        print('listening for connection ....')
        addr,conn=soc.accept()
        thread= threading.Thread(target= userhandler,args=(conn, addr))
        thread.start()


def start():
    acceptcon()


start()