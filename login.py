#!/usr/bin/python3

#login termux


from hashlib import md5,sha1,sha224,sha384,sha256,sha512
from os import system
from signal import signal, SIGINT, SIGTSTP, SIGQUIT
from time import sleep
from getpass import getpass
from sys import exit


a = sha512("md5".encode('utf8')).hexdigest()
b = sha512("sha1".encode('utf8')).hexdigest()
c = sha512("sha224".encode('utf8')).hexdigest()
d = sha512("sha256".encode('utf8')).hexdigest()
e = sha512("sha384".encode('utf8')).hexdigest()
f = sha512("sha512".encode('utf8')).hexdigest()
validator_correct_execute_banner = False
signal_counter = 0
MAX_SIGNAL_ATTEMPTS = 1
figlet = ["big.flf","banner.flf","digital.flf","small.flf","slant.flf","shadow.flf","smscript.flf","smslant.flf","block.flf","bubble.flf"]


def exit_console():
   '''
     funcion la cual me permite cerrar la seccion en termux
   '''
   #comando en shell bash el cual me permite saber cual es el PID de la consola activa y cerrarla
   system("""
              shell_PDI=$(ps | grep bash | cut -d'p' -f1 )
              kill -9 $shell_PDI
           """)

def banner():
    '''
     funcion la cual me permite agregar un banner en bash con figlet y neofetch y tambien verificar si es valido
    '''
    rute_banner_read="/data/data/com.termux/files/home/login_python3/.banner.txt"
    with open(rute_banner_read,'r',encoding="utf8") as banner_file_config:
       banner_file_read=banner_file_config.read().strip()
    
    #permite verificar si el banner establecido por el usuario es valido con la lista de banners disponibles
    if banner_file_read in figlet:
       global validator_correct_execute_banner
       validator_correct_execute_banner=True
       system("bash /data/data/com.termux/files/home/login_python3/.figlet.sh")
       print("""

             """)
    else:
        system("clear")
        print("¡Banner invalido!")
        sleep(3)
        system("clear")
        print("NOTA:¡Ejecute primero el archivo dependencias.sh!")
        sleep(3)
        exit_console()
  

def signal_esc(sig,frame):
   '''
       funcion la cual me permite atrapar teclas de salida con el modulo signal
   '''
   print("\nAcesso no consedido! ")
   sleep(1)
   global signal_counter
   signal_counter += 1
   if signal_counter >= MAX_SIGNAL_ATTEMPTS:
        print("Demasiados intentos de señales. Saliendo del programa.")
        exit_console()
   else:
        main()


def password_local():
      '''
         funcion la cual me permite leer la contraseña localmente almacenada en el directorio login
      '''
      rute_complete_password_local="/data/data/com.termux/files/home/login_python3/.password_user.txt"
      with open(rute_complete_password_local,'r',encoding="utf8") as file_read_password_local:
           password_local=file_read_password_local.read()
      return password_local


def validator_hash(hash_select_validator):
      '''
        funcion donde comparo el hash seleccionado con una lista de hash para verificar si es valido y por medio de eso codificar la contrasena entrante del usuario
      '''
      global password
      if hash_select_validator in [a,b,c,d,e,f] and validator_correct_execute_banner:
        password=getpass("Ingrese su contraseña: ")
        if hash_select_validator == a:
           password=md5(password.encode('utf8')).hexdigest()
        elif hash_select_validator == b:
          password=sha1(password.encode('utf8')).hexdigest()
        elif hash_select_validator == c:
           password=sha224(password.encode('utf8')).hexdigest()
        elif hash_select_validator == d:
           password=sha256(password.encode('utf8')).hexdigest()
        elif hash_select_validator == e:
           password=sha384(password.encode('utf8')).hexdigest()
        elif hash_select_validator == f:
           password=sha512(password.encode('utf8')).hexdigest()
      else:
        system("clear")
        print("¡ADVERTENCIA:Hash invalido!")
        sleep(3)
        exit_console()
      

def main():
    '''
       funcion donde agrego un contador para controlar los intentos de inicio de seccion y con base a eso aplicar proteccion contra fuerza bruta y tambien se compara la contrasena para verificar si es correcta
    '''
    try:
      signal(SIGINT, signal_esc)
      signal(SIGTSTP, signal_esc)
      signal(SIGQUIT, signal_esc)
      counter=10
      for interation in range(10):
        counter -= 1
        system("clear")
        banner()
        rute_complete_hash_select="/data/data/com.termux/files/home/login_python3/.hash_selection.txt"
        with open(rute_complete_hash_select,'r',encoding="utf8") as file_read_hash_select:
          hash_select_validator=file_read_hash_select.read()
        validator_hash(hash_select_validator)
        if password == password_local():
             print("Acceso concedido!")
             exit(1)
        else:
             system("clear")
             print("¡CONTRASEÑA INVALIDA!")
             print(f"Intentos disponibles => {counter}")
             sleep(3)
             if interation == 9:
                exit_console()
    except FileNotFoundError as e:
       print(f"file does not exist => {e}")
       

if __name__ == "__main__":
    try:
        main()
    except EOFError:
        exit_console()

__name__="Login Termux"
__version__="1.0"
__author__="whitehack"
__status__="Finish"
__license__="GPL"
