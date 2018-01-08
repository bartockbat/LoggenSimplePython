# Glen Millard glenmillard@gmail.com
#This hopefully will run in most environments. I use it in Cygwin and Python
#You may need to modify it to your environment with the path of the python interpreter
#I have it running 10 000 times in a loop - sole purpose it to fill up your SSB box
#!/usr/bin/python
# loggen -r 10 -i -d -D -F --file-read-file=2/'1(10035).txt' 10.21.145.12 514 - sample loggen run
import os
for x in range (1,100000):
    os.system("loggen -iS -r 10000000 -s 200 -I 600 --active-connections=1 --idle-connections=1 10.0.0.20 514")
    #os.system("loggen -iS -r 10000000 -s 200 -I 600 --active-connections=1 --idle-connections=1 10.21.255.148 514")
    #os.system("loggen -iS -r 10000000 -s 200 -I 600 --active-connections=1 --idle-connections=1 10.21.145.12 514")
