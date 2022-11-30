# Funciones comunes
from cryptography.fernet import Fernet


def encriptar(dato, key):
	fernet = Fernet(bytes(key))
	encriptado = fernet.encrypt(dato.encode())
	return encriptado
def desencriptar(dato, key):
	fernet = Fernet(bytes(key))
	desencriptado = fernet.decrypt(dato).decode()
	return desencriptado

def escribir(dato): # Dato es un array con todas las str que se quieran grabar
	dpg = open("datos_de_programa.txt","a+") # Añade datos y lee, pero no sobreescribe
	dpg.writelines(dpg)
	dpg.close()

def leer(linea, key):
	dpg = open("datos_de_programa.txt", "a+")
	lectura = desencriptar(dpg.readline(linea), bytes(key))
	dpg.close()
	return lectura