#!/usr/bin/python3


from hashlib import md5,sha1,sha224,sha256,sha384,sha512
from os import system
from time import sleep
from sys import exit



def save_password(password_user_hash,password_hash_uninstall):
       '''
           funcion la cual guardara la contraseña codificada del usuario
       '''
       rute_complete_save_password="/data/data/com.termux/files/home/login_python3/.password_user.txt"
       with open(rute_complete_save_password,'w') as archive_write:
          archive_write.write(password_user_hash)
       password_hash_uninstall_hash=sha512(password_hash_uninstall.encode('utf8')).hexdigest()
       rute_complete_hash_password_uninstall="/data/data/com.termux/files/home/login_python3/.password_hash_uninstall.txt"
       with open(rute_complete_hash_password_uninstall,'w') as archive_write:
          archive_write.write(password_hash_uninstall_hash)
       print("""
(NOTA:¡Las dos contraseñas se almacenaron en login_python3 como (.password_user.txt/.password_hash_uninstall.txt)!
              """)
       sleep(7)
       system("clear")


def input_password_user():
 '''
   funcion que pedira y codificara una contraseña brindada por el usuario.
 '''
 try:
   a=sha512("md5".encode('utf8')).hexdigest()
   b=sha512("sha1".encode('utf8')).hexdigest()
   c=sha512("sha224".encode('utf8')).hexdigest()
   d=sha512("sha256".encode('utf8')).hexdigest()
   e=sha512("sha384".encode('utf8')).hexdigest()
   f=sha512("sha512".encode('utf8')).hexdigest()
   print("CONSEJO: (¡usar contraseñas > 8 caracteres y que sea Aleatoria)")
   password_user=input("ingrese la contraseña de tu login: ")
   sleep(1)
   system("clear")
   password_hash_uninstall=input("ingrese la contraseña de eliminacion de el login: ")
   sleep(1)
   system("clear")
   print("""
 -------------------------------------------------------
|      Elige un hash para codificar la contraseña       |
 -------------------------------------------------------
       |  Lista de hashes: |
       |    md5            |
       |    sha1           |
       |    sha224         |
       |    sha256         |
       |    sha384         |
       |    sha512         |
        -------------------
NOTA:El hash md5 y sha-1 son vulnerables a (\"colisiones\",\"fuerza bruta\")
""",end="")

   while True:
    hash=input("Escriba el hash a elegir: ").lower().strip()
    hash=sha512(hash.encode('utf8')).hexdigest()
    if hash and hash in [a,b,c,d,e,f]:
      print("¡Hash valido!")
      sleep(1)
      system("clear")
      break
    else:
       system("clear")
       print("¡Ingresaste un hash invalido!")
       sleep(2)

   rute_complete_save_hash="/data/data/com.termux/files/home/login_python3/.hash_selection.txt"
   with open(rute_complete_save_hash,'w') as archive_write:
      archive_write.write(hash)
   
   if hash == a:
       password_user_hash=md5(password_user.encode('utf8')).hexdigest()
       save_password(password_user_hash,password_hash_uninstall)
   elif hash == b:
      password_user_hash=sha1(password_user.encode('utf8')).hexdigest()
      save_password(password_user_hash,password_hash_uninstall)
   elif hash == c:
      password_user_hash=sha224(password_user.encode('utf8')).hexdigest()
      save_password(password_user_hash,password_hash_uninstall)
   elif hash == d:
      password_user_hash=sha256(password_user.encode('utf8')).hexdigest()
      save_password(password_user_hash,password_hash_uninstall)
   elif hash == e:
      password_user_hash=sha384(password_user.encode('utf8')).hexdigest()
      save_password(password_user_hash,password_hash_uninstall)
   elif hash == f:
      password_user_hash=sha512(password_user.encode('utf8')).hexdigest()
      save_password(password_user_hash,password_hash_uninstall)
  
 except KeyboardInterrupt:
     system("clear")
     print("saliendo del script \"hash_pass.py\"")
     exit(2)


if __name__ == "__main__":
     input_password_user()
