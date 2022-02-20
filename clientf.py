import datetime
import socket
import sys
from time import sleep


ip = "127.0.0.1"
port = 1443
buff = 4096
i = 0
n = 10
data = []
dic = {}

glist = []

# Create socket for server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s_1.bind(("", 7004))
# Let's send data through UDP protocol
begin_time = datetime.datetime.now()
tup = (ip, port)

def helper(x):
    while(len(x)<8):
        x = str(0) + x
    return x
   
def sender(l,r):
    for i in range(l,r+1):
        i_byt = bytes(helper(str(i)),'utf-8')
        i_data = i_byt + data[i]
        s.sendto(i_data,tup)

#def resending():
#    data_r, address = s.recvfrom(4096)
#    index = int(data_r)
#    s.sendto(data[index],tup)
    
try:
    print("Enter File name")
    k = input()
    file = open(k,'r+b')
    send_data = file.read(buff)
    while send_data:
        data.append(send_data)
        send_data = file.read(buff)
        i += 1
    i = 0
    while i<len(data):
        sender(i,min(i+n-1,len(data)-1))
        i += n
    # while send_data:
    #    i_byt = bytes(helper(str(i)),'utf-8')
    #    i_data = i_byt + send_data
    #    s.sendto(i_data,tup)
    #    dic[i] = send_data
    #    send_data = file.read(buff)
    #    i += 1
    print(f"Time taken to send file is : {datetime.datetime.now() - begin_time} s")
    print("Client sent the file")
    file.close()
    print(f"Size of file sent was {i * buff}")
    #sleep(0.1)
    stop = bytes(helper(str(102411)),'utf-8') 
    s.sendto(stop,tup)

    try:
        print("listening")
        data_l,address = s_1.recvfrom(4096)
        print(int(data_l[:8]))
#        for i in range(int(data[:8])):
#            resending()
    except:
        print("no ack received")
except KeyboardInterrupt:
    # data_l,address = s.recvfrom(4096)
    # print(int(data_l[:8]))
    # for i in range(int(data[:8])):
    #     resending()
    print("78")
    s.close()
    s_1.close
