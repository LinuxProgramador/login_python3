#!/bin/python3


from hashlib import md5,sha1,sha224,sha256,sha384,sha512
from os import system
from time import sleep




def input_password_user():
  '''
   funcion la cual codificara una contraseña
  '''


  a=sha512("md5".encode('utf8')).hexdigest()
  b=sha512("sha1".encode('utf8')).hexdigest()
  c=sha512("sha224".encode('utf8')).hexdigest()
  d=sha512("sha256".encode('utf8')).hexdigest()
  e=sha512("sha384".encode('utf8')).hexdigest()
  f=sha512("sha512".encode('utf8')).hexdigest()



  password_user=input("ingresa la contrasena de tu login: ")
  sleep(1)
  system("clear")

  print("""
Elige un hash para codificar la contraseña
Lista de hashes:
        md5
        sha1
        sha224
        sha256
        sha384
        sha512

NOTA: el hash md5 y sha1 son vulnerables a ataques
""")

  hash=input("escriba el hash a elegir: ").lower()
  hash.strip()
  sleep(1)
  hash=sha512(hash.encode('utf8')).hexdigest()
  system("clear")

  rute_complete_2="/data/data/com.termux/files/home/login_python3/.hash_selection.txt"
  archive_write=open(rute_complete_2,'w')
  archive_write.write(hash)
  archive_write.close()



  def almacenar(password_user_hash):
       '''
           funcion la cual almacenara una contrasena codificada
       '''

       rute_complete="/data/data/com.termux/files/home/login_python3/.password_user.txt"
       archive_write=open(rute_complete,'w')
       archive_write.write(password_user_hash)
       archive_write.close()

       print("""
NOTA: La contrasena se almaceno como un archivo oculto llamado .password_user.txt en el directorio login
              """)
       sleep(5)
       system("clear")

       return




  if hash == a:
       password_user_hash=md5(password_user.encode('utf8')).hexdigest()
       almacenar(password_user_hash)


  elif hash == b:

      password_user_hash=sha1(password_user.encode('utf8')).hexdigest()
      almacenar(password_user_hash)

  elif hash == c:
      password_user_hash=sha224(password_user.encode('utf8')).hexdigest()
      almacenar(password_user_hash)


  elif hash == d:
      password_user_hash=sha256(password_user.encode('utf8')).hexdigest()
      almacenar(password_user_hash)

  elif hash == e:
      password_user_hash=sha384(password_user.encode('utf8')).hexdigest()
      almacenar(password_user_hash)


  elif hash == f:
      password_user_hash=sha512(password_user.encode('utf8')).hexdigest()
      almacenar(password_user_hash)


  return




input_password_user()
