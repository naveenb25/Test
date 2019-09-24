#!/usr/bin/python3
from time import ctime,sleep
from subprocess import getstatusoutput,getoutput
from os import mkdir
options='''
press 1 to print date and time.
press 2 to run OS command
press 3 to create a directory
'''
print(options)
choice=input()
print("you have choosen ", choice)
if choice == '1' :
    print(ctime())
elif int(choice) ==2:
    cmd=input("please enter any command : ")
    output=getoutput(cmd)
    print(output)
elif choice == '3':
    d_name=input("enter directory name to create: ")
    mkdir(d_name)
    print(d_name,"successfully created")
elif choice == '4':
    web=input("")
    print(getouput("ping -c 5 "web))
else:
    print("wrong input") 
