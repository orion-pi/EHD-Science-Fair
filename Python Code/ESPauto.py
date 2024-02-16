import socket
import time

TCP_IP = '192.168.4.1'
TCP_PORT = 8888
BUFFER_SIZE = 1024
run = True
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
zero = 0
while run:
    num = input()
    if (num == "e"):
        run = False
    elif (num == "z"):
        s.send(b"c")
        data = (s.recv(BUFFER_SIZE)).decode("utf-8")
        zero = float(data)
        print(data)
    elif num.isnumeric() :
        for i in range(int(num)):
            s.send(b"c")
            data = (s.recv(BUFFER_SIZE)).decode("utf-8")
            print((zero-float(data))*-9.096918610635759e-06)
            time.sleep(0.5)
        print("done")
        
s.close()

