import os

c = input("Canal > ")
bssid = input("AP MAC > ")
log = input("Nombre del log > ")
interfaz = input("Interfaz > ")

os.system("airodump-ng --channel " + c + " --bssid " + bssid + " --write " + log + " " + interfaz)

