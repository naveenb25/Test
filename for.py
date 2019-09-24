
#!/usr/bin/python3
from subprocess import getoutput 
import sys
data=sys.argv[1:]
for i in data:
    print(getoutput("ping -c 3 "+i))
