#!/usr/bin/python3
import paramiko,time,sys
#using as ssh client
client=paramiko.SSHClient()
#auto adjust host key verificaito with yes or no
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#connected with ssh session
device_ip=["172.16.6.131","172.16.6.131","172.16.6.131"] 
u='root'
p='cisco'
#apply for loop
for i in device_ip:
    client.connect(i,username=u,password=p,allow_agent=False, look_for_keys=False)
    device_access=client.invoke_shell()
    device_access.send("show ip int brief\n")
    time.sleep(0.5)
    output=device_access.recv(65000)
    print(type(output))
    print(output.decode('ascii'))
    with open(i+time.ctime(),'w')as f:
        f.write(output.decode('ascii'))
        time.sleep(1)

