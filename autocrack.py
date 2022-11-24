import os
import subprocess
import time

directorioTrabajo = os.getcwd()
def abrir(script): 
	subprocess.Popen(['qterminal', '-e', script])
	time.sleep(0.5)

def salir(inter):
	os.system("clear")
	print("Apagando " + inter + " ...")
	os.system("ifconfig " + inter + " down")
	print("Deshabilitando el modo monitor ...")
	try:
		os.system("airmon-ng stop " + inter)
	except:
		print("Reintentando ...")
		print("Restaurando modo managed ...")
		os.system("iwconfig " + inter + " mode managed")	
	print("Volviendo a encender la interfaz " + inter + " ...")
	os.system("ifconfig " + inter + " up")
	print("Reiniciando servicio de red ...")
	os.system("service networking restart")
	print("Reiniciando administrador de redes ...")
	os.system("service NetworkManager restart")

	

	
	print("\n\nHasta la vista, baby!")
	time.sleep(1)

def main(msg, inter):
	os.system("clear")
	print("===========================================")
	print("            1 - Escucha.")
	print("            2 - Desautenticación.")
	print("            3 - Captura.")
	print("            4 - Vistazo.")
	print("            0 - Salir.")
	print("===========================================")
	print(msg)
	opcion = input("\n >>> ")
	if opcion == "0":
		salir(inter);
	elif opcion == "1":
		script = 'python ' + directorioTrabajo + '/modulos/escucha.py'
		try:
			abrir(script)
		except:
			main("No se pudo ejecutar script de escucha.",inter)
		finally:
			main("Abierto script de escucha.",inter)
	elif opcion == "2":
		script = 'python ' + directorioTrabajo + '/modulos/desautenticacion.py'
		try:
			abrir(script)
		except:
			main("No se pudo ejecutar script de desautenticación.",inter)
		finally:
			main("Abierto script de desautenticación.",inter)
		
	elif opcion == "3":
		script = 'python ' + directorioTrabajo + '/modulos/captura.py'
		try:
			abrir(script)
		except:
			main("No se pudo ejecutar script de captura.",inter)
		finally:
			main("Abierto script de captura.",inter)
	elif opcion == "4":
		script = 'python ' + directorioTrabajo + '/modulos/vistazo.py'
		try:
			abrir(script)
		except:
			main("No se pudo ejecutar script de desautenticación.",inter)
		finally:
			main("Abierto script de desautenticación.",inter)
	else:
		fallo = "'" + opcion + "' no es una opción válida!"
		main(fallo, inter)

if os.geteuid() != 0:
	exit("Debes ser superusuario!")
os.system("airmon-ng check kill")
os.system("airmon-ng")
interfaz = input("\n\nIntroduce la interfaz > ")
os.system("airmon-ng start " + interfaz)
main("",interfaz)



