from ast import While
#from asyncio import threads
import socket
import sys
from time import sleep
from threading import Thread

ip = "127.0.0.1"
port = 1443
packets = 25600
l = []
total = [i for i in range(packets)]
lst = []
d = {}
Missing = []
string = ""
Threads = []

def helper(x):
    while(len(x)<8):
        x = str(0) + x
    return x
   
# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
tup = (ip,7004)
# Bind the socket to the port
server_address = (ip, port)
s.bind(server_address)
binary_file=open("my_file", "wb")
print("Data to be recieved")

# def req(t):
#     for i in range(len(t)):
#         temp = bytes(helper(str(i)),'utf-8') 
#         s.sendto(temp,server_address)
#     temp_1 = bytes(helper(str(100000000)),'utf-8')
#     s.sendto(temp_1,server_address)

# def MissingRecieving():
#     while True:
#         data, address = s.recvfrom(4096)
#         if int(data[:8]) > 102401:
#             break
#         #data_id, address_id = s.recvfrom(1024)
#         t = int(data[:8])
#         if t in Missing:
#             Missing.remove(t)
#         d[t] = data[8:]

# t1 = Thread(target=req,args=(Missing,))
# t2 = Thread(target=MissingRecieving)

curr_i = 0
try:
    while True:
        data, address = s.recvfrom(4096)
        #data_id, address_id = s.recvfrom(1024)
        t = int(data[:8])
        # if t<10:
        #     print(data)
        if int(data[:8]) > 102401:
            print(t)
            break
        d[t] = data[8:]
        while curr_i < t:
            Missing.append(curr_i)
            curr_i +=1
        curr_i += 1
        l.append(t)
        # binary_file.write(data[8:])
#    print(len(Missing))
    l_Missing = bytes(helper(str(2000)),'utf-8')

#    l_Missing_d = bytes(helper(str(len(Missing) +10)),'utf-8')
    
    sleep(1)
    print("ack is sent")
#    s_1.sendto(l_Missing_d,tup)

    s_1.sendto(l_Missing,tup)
    print(l_Missing)

    # t1.start()
    # t2.start()

    # while(len(Missing) > 0):
    #     t1.join()
    #     t2.join()
    # req(Missing)

    # for m in Missing:
    #     string += str(m) + ","
    # print(string)
    # Str_bytes = bytes(string,'utf-8')
    # print(len(Str_bytes))
    # s.sendto(Str_bytes,server_address)
except KeyboardInterrupt:
    print("\n")
    print(f" last element is {l[len(l) - 1]}")
    print(f" length of l is {len(l)}")
    print("\n")
    s.close()

