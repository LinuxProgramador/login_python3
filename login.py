#!/bin/python3

#login


from hashlib import md5,sha1,sha224,sha384,sha256,sha512
from os import system
import signal
from time import sleep
from getpass import getpass


a=sha512("md5".encode('utf8')).hexdigest()
b=sha512("sha1".encode('utf8')).hexdigest()
c=sha512("sha224".encode('utf8')).hexdigest()
d=sha512("sha256".encode('utf8')).hexdigest()
e=sha512("sha384".encode('utf8')).hexdigest()
f=sha512("sha512".encode('utf8')).hexdigest()




def exit_console():
   '''
     funcion la cual me permite cerrar la seccion
   '''
   system("""
              shell_PDI=$(ps | grep bash | cut -d'p' -f1 )
              kill -9 $shell_PDI
           """)



def banner():
   '''
     funcion la cual me permite agregar un banner en bash con figlet
   '''
   system("bash /data/data/com.termux/files/home/login_python3/.figlet.sh")
   print("""

         """)
   return




def signal_esc(sig,frame):
   '''
       funcion la cual me permite atrapar teclas de salida
   '''
   print("\nacesso no consedido! ")
   sleep(1)
   global signal_counter
   signal_counter += 1
   if signal_counter >= MAX_SIGNAL_ATTEMPTS:
        print("Demasiados intentos de señales. Saliendo del programa.")
        exit_console()
   else:
        main()





def password_hash():
   '''
     funcion la cual me permite ingresar una contraseña y hashearla para comprobarla
   '''


   rute_complete_3="/data/data/com.termux/files/home/login_python3/.hash_selection.txt"
   archivo_leer3=open(rute_complete_3,'r',encoding="utf8")
   hash_4=archivo_leer3.read()

   if hash_4 in [a,b,c,d,e,f]:

     password=getpass("ingrese su contraseña: ")
     if hash_4 == a:
        password=md5(password.encode('utf8')).hexdigest()


     elif hash_4 == b:

        password=sha1(password.encode('utf8')).hexdigest()

     elif hash_4 == c:

        password=sha224(password.encode('utf8')).hexdigest()



     elif hash_4 == d:
        password=sha256(password.encode('utf8')).hexdigest()


     elif hash_4 == e:
        password=sha384(password.encode('utf8')).hexdigest()



     elif hash_4 == f:
        password=sha512(password.encode('utf8')).hexdigest()

   else:
      exit_console()

   return password




def password_local():
   '''
      funcion la cual me permite comprobar la contraseña por medio de un hash sha512 local de contraseña
   '''
   try:
     ruta_completa="/data/data/com.termux/files/home/login_python3/.password_user.txt"
     leer_archivo=open(ruta_completa,'r',encoding="utf8")
     password_local=leer_archivo.read()
     return password_local


   except FileNotFoundError:
     print("el archivo donde esta la contraseña no existe")
     sleep(3)
     system("clear")
     print("ejecute primero el archivo dependencias.sh con bash dependencias.sh y vuelva a intentar ejecutar este programa despues de cerrarse esta seccion")
     sleep(5)
     exit_console()





def main():
  '''
     funcion principal la cual me permite llamar otras funciones y especificar el codigo importante
  '''
  temporizador=0
  while True:

    system("clear")
    banner()
    if password_hash() == password_local():
       print("acceso concedido!")
       break

    else:
       print("¡contraseña invalida!")
       temporizador += 1
       print(f"¡intentos disponibles {10-temporizador} antes de que se cierre!")
       sleep(3)
       if temporizador > 10:
          exit_console()





if __name__ == "__main__":
  signal_counter=0
  MAX_SIGNAL_ATTEMPTS=2
  while True:
    signal.signal(signal.SIGINT, signal_esc)
    signal.signal(signal.SIGTSTP, signal_esc)
    signal.signal(signal.SIGQUIT, signal_esc)
    try:
          main()
          break
    except EOFError:
          system("""
                  shell_PDI=$(ps | grep bash | cut -d'p' -f1 )
                  kill -9 $shell_PDI
                 """)






__name__="Login"
__version__="1.0"
__maintainer__="Anonimous"
__author__="Anonimous"
__status__="finish"
__email__="Anonimous01011001@gmail.com"
__license__="GPL"
__copyright__="Anonimous Inc."
