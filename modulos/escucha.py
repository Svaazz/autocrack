import os
import sys
from comun import *
key = sys.argv[1]
interfaz = leer(0, key)
os.system("clear")
os.system("airodump-ng " + interfaz)
