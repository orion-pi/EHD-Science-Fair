import socket
import matplotlib

import matplotlib.pyplot as plt
from scipy import stats

TCP_IP = '192.168.4.1'
TCP_PORT = 8888
BUFFER_SIZE = 1024
x = []
y = []
run = True
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while run:
    weight = input("Weight to calibration for? (type e to exit)")
    if (weight == "e"):
        run = False
    else:
        s.send(b"c")
        data = (s.recv(BUFFER_SIZE)).decode("utf-8")
        print(data)
        x.append(float(data))
        y.append(float(weight))
print(x, y)
s.close()
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x): 
  return slope * x + intercept    

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

print(r, r**2)
print(slope)
print(intercept)
