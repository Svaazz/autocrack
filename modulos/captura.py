import os
import sys

interfaz = sys.argv[1]


c = input("Canal > ")
bssid = input("AP MAC > ")
log = input("Nombre del log > ")

os.system("airodump-ng --channel " + c + " --bssid " + bssid + " --write /logs/" + log + " " + interfaz)
op = input("Reintentar? s/n > ")
