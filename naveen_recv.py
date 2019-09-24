#!/usr/bin/python3
import socket,time
#checking for socket functions
print([i for i in dir(socket) if 'socket' in i])
#now creating udp socket
#ipv4 socket -- ipv4 + 2 byte port
#ipv6 socket -- ipv6 + 2 byte port
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #for tcp

s.bind(("",8891))
#bind will accept tuple format ip & port
while True:
    data=s.recvfrom(1000)
    print(data)

#sender
#enter message
#msf=input("enter data to send : ")
#convert data into byte-like string format
#newmsg=msg.encode('ascii')
#s.sendto(newmsg,("127.0.0.1",8889))
#s.close()

