#!/usr/bin/python3


from hashlib import md5,sha1,sha224,sha256,sha384,sha512
from os import system
from time import sleep
import sys



def input_password_user():
 '''
   funcion la cual pedira y codificara una contraseña brindada por el usuario en algun hash elegido
 '''
 try:

   a=sha512("md5".encode('utf8')).hexdigest()
   b=sha512("sha1".encode('utf8')).hexdigest()
   c=sha512("sha224".encode('utf8')).hexdigest()
   d=sha512("sha256".encode('utf8')).hexdigest()
   e=sha512("sha384".encode('utf8')).hexdigest()
   f=sha512("sha512".encode('utf8')).hexdigest()


   print("CONSEJO:(¡usar contraseñas > 8 caracteres y que tengan Números,Símbolos,Mayusculas,Minusculas!)")
   password_user=input("ingresa la contrasena de tu login: ")
   sleep(1)
   system("clear")

   password_hash_uninstall=input("ingresa la contrasena de eliminacion de el login: ")
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
    if bool(hash) != False and hash in [a,b,c,d,e,f]:
      print("¡Hash valido!")
      sleep(1)
      system("clear")
      break

    else:
       system("clear")
       print("¡Ingresaste un hash invalido!")
       sleep(2)



   rute_complete_save_hash="/data/data/com.termux/files/home/login_python3/.hash_selection.txt"
   archive_write=open(rute_complete_save_hash,'w')
   archive_write.write(hash)
   archive_write.close()



   def save_password(password_user_hash,password_hash_uninstall):
       '''
           funcion la cual guardara la contrasena codificada del usuario
       '''

       rute_complete_save_password="/data/data/com.termux/files/home/login_python3/.password_user.txt"
       archive_write=open(rute_complete_save_password,'w')
       archive_write.write(password_user_hash)
       archive_write.close()

       password_hash_uninstall_hash=sha512(password_hash_uninstall.encode('utf8')).hexdigest()
       rute_complete_hash_password_uninstall="/data/data/com.termux/files/home/login_python3/.password_hash_uninstall.txt"
       archive_write=open(rute_complete_hash_password_uninstall,'w')
       archive_write.write(password_hash_uninstall_hash)
       archive_write.close()


       print("""
(NOTA:¡Las dos contrasenas se almacenaron en el directorio login_python3 como (.password_user.txt/.password_hash_uninstall.txt)!
              """)
       sleep(5)
       system("clear")

       return




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


   return

 except KeyboardInterrupt:
     system("clear")
     print("saliendo del script \"hash_pass.py\"")
     sys.exit(2)


if __name__ == "__main__":
     input_password_user()
