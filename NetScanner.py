import os,subprocess

def main():
	miDireccion = raw_input("direccion: ")

	for p in range(0,256):
		ip = '192.168.0.'+str(p) #tener en cuenta que la direccion puede variar segun el modem/router

		saver = open('temp.txt','w')
		subprocess.call(['ping','-n','1',ip],stdout=saver)
		saver.close()

		leerSaver = open('temp.txt','r')
		linea = leerSaver.readlines()

		estado = linea[2]

		wrong = "Reply from "+ miDireccion +": Destination host unreachable.\n"
		

		if estado == wrong:
			pass
		else: 
			data = "[+] El host " + ip + " se encuentra activo.\n"
			dataSaver = open('hostActivos.txt','a')
			dataSaver.write(data)
			dataSaver.close()

			print data
			
main()
