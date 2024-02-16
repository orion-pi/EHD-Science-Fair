import socket


TCP_IP = '192.168.4.1'
TCP_PORT = 8888
BUFFER_SIZE = 1024
run = True
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
zero = 0
while run:
    weight = input()
    if (weight == "e"):
        run = False
    if (weight == "z"):
        s.send(b"c")
        data = (s.recv(BUFFER_SIZE)).decode("utf-8")
        zero = float(data)
        print(data)
    if (weight == "m"):
        s.send(b"c")
        data = (s.recv(BUFFER_SIZE)).decode("utf-8")
        print((zero-float(data))*-9.096918610635759e-06)
        
s.close()

