#!/usr/bin/python3
import paramiko,time,sys
#using as ssh client
client=paramiko.SSHClient()
#auto adjust host key verificaito with yes or no
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
addr=input("enter yor router IP:")
u='root'
p='cisco'
#connected with ssh session
client.connect(addr,username=u,password=p,allow_agent=False, look_for_keys=False)
#we have to ask for shell
device_access=client.invoke_shell()
device_access.send("show ip int brief\n")
time.sleep(0.5)
output=device_access.recv(65000)
print(type(output))
print(output.decode('ascii'))

