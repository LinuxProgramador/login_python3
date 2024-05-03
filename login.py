#!/usr/bin/python3

#login termux


from hashlib import md5,sha1,sha224,sha384,sha256,sha512
from os import system
import signal
from time import sleep
from getpass import getpass
import sys



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
     funcion la cual me permite agregar un banner en bash con figlet y neofetch y tambien verificara si el ingresado por el usuario es valido
 '''
 try:

    rute_banner_read="/data/data/com.termux/files/home/login_python3/.banner.txt"
    banner_file_config=open(rute_banner_read,'r',encoding="utf8")
    banner_file_read=banner_file_config.read().strip()
    banner_file_config.close()


    #me permite verificar si el banner establecido por el usuario es valido con la lista de banners disponibles
    if banner_file_read in ["big.flf","banner.flf","digital.flf","small.flf","slant.flf","shadow.flf","smscript.flf","smslant.flf","block.flf","bubble.flf"]:

       validator_correct_execute_banner="perfect"
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
        system("""
              shell_PDI=$(ps | grep bash | cut -d'p' -f1 )
              kill -9 $shell_PDI
           """)


 except FileNotFoundError:
        print("¡Valores no existentes!")
        sleep(2)
        print("NOTA:¡Ejecute primero el archivo dependencias.sh")
        system("""
              shell_PDI=$(ps | grep bash | cut -d'p' -f1 )
              kill -9 $shell_PDI
           """)


 return




def validator_files():
   '''
     funcion la cual me permite validar la existencia de archivos localmente para la correcta funcionalidad del login
   '''

   #me valida la existencia de los archivos nesesarios para el correcto funcionamiento del programa login termux y tambien elimina archivo basura que se encuentren en el directorio login_python3
   system("ls -a ~/login_python3/ | grep -v .banner.txt | grep -v .hash_selection.txt | grep -v .usuario.txt | grep -v .password_user.txt | grep -v .lista_local.txt | grep -v dependencias.sh | grep -v README.md | grep -v hash_pass.py | grep -v login.py | grep -v .figlet.sh | grep -v .borrador.txt | grep -v .password_hash_uninstall.txt | grep -v uninstall.sh | grep -v .hash_uninstall.py | grep -v LICENSE  | grep -v motd | grep -v motd1 >  ~/login_python3/.borrador.txt ")
   system("cat ~/login_python3/.borrador.txt | xargs rm -f")

   system("ls -a ~/login_python3/ | grep .txt | grep -v .lista_local.txt | grep -v .borrador.txt | grep -v .password_hash_uninstall.txt > ~/login_python3/.lista_local.txt")
   rute_complete_list="/data/data/com.termux/files/home/login_python3/.lista_local.txt"

   file_list=open(rute_complete_list,'r',encoding="utf8")
   list_local=file_list.read().strip()
   file_list.close()
   variable_local="""
.banner.txt
.hash_selection.txt
.password_user.txt
.usuario.txt
"""

   if list_local == variable_local.strip() :
       pass

   else:
       system("clear")
       print("ADVERTENCIA:archivos no encontrados en el directorio login!")
       sleep(3)
       system("clear")
       print("NOTA:¡Ejecute primero el archivo dependencias.sh!")
       sleep(4)
       exit_console()

   return




def signal_esc(sig,frame):
   '''
       funcion la cual me permite atrapar teclas de salida con el modulo signal
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





def password_local():
      '''
         funcion la cual me permite leer la contraseña localmente almacenada en el directorio login
      '''

      rute_complete_password_local="/data/data/com.termux/files/home/login_python3/.password_user.txt"
      file_read_password_local=open(rute_complete_password_local,'r',encoding="utf8")
      password_local=file_read_password_local.read()
      return password_local




def main():
    '''
       funcion donde agrego un contador para controlar los intentos de inicio de seccion y con base a eso aplicar proteccion contra fuerza bruta y tambien se compara la contrasena para verificar si es correcta
    '''
    def validator_hash():
      '''
        funcion donde comparo el hash seleccionado con una lista de hash para verificar si es valido y por medio de eso codificar la contrasena entrante del usuario
      '''

      global password

      if hash_select_validator in [a,b,c,d,e,f] and bool(validator_correct_execute_banner) != False:

        password=getpass("ingrese su contraseña: ")
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

      return



    counter=11
    for interation in range(13):

        counter -= 1
        system("clear")
        banner()

        rute_complete_hash_select="/data/data/com.termux/files/home/login_python3/.hash_selection.txt"
        file_read_hash_select=open(rute_complete_hash_select,'r',encoding="utf8")
        hash_select_validator=file_read_hash_select.read()

        validator_hash()
        if password == password_local():
             print("acceso concedido!")
             sys.exit(1)



        else:
             system("clear")
             print("¡contraseña invalida!")
             print(f"¡intentos disponibles {counter}!")
             sleep(3)
             if interation >= 10:
                exit_console()





if __name__ == "__main__":

  validator_correct_execute_banner=" "
  a=sha512("md5".encode('utf8')).hexdigest()
  b=sha512("sha1".encode('utf8')).hexdigest()
  c=sha512("sha224".encode('utf8')).hexdigest()
  d=sha512("sha256".encode('utf8')).hexdigest()
  e=sha512("sha384".encode('utf8')).hexdigest()
  f=sha512("sha512".encode('utf8')).hexdigest()

  signal_counter=0
  MAX_SIGNAL_ATTEMPTS=1

  while True:
    signal.signal(signal.SIGINT, signal_esc)
    signal.signal(signal.SIGTSTP, signal_esc)
    signal.signal(signal.SIGQUIT, signal_esc)

    try:

          validator_files()
          main()
          break
    except EOFError:
          system("""
                  shell_PDI=$(ps | grep bash | cut -d'p' -f1 )
                  kill -9 $shell_PDI
                 """)






__name__="Login Termux"
__version__="1.0"
__maintainer__="white hack"
__author__="white hack"
__status__="finish"
__email__="NULL"
__license__="GPL"
__copyright__="NULL"
