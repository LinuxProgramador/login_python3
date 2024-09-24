#!/usr/bin/python3

from hashlib import sha512
from getpass import getpass
from sys import exit


def input_password_hash_delete():
     '''
       funcion la cual tomara la contraseña y la codificara para proceder a eliminar el login termux
     '''
     try:
       password_hash_delete=getpass("ingrese su contraseña para eliminar el login: ")
       password_hash_delete=sha512(password_hash_delete.encode('utf8')).hexdigest()
       print(password_hash_delete)
     except KeyboardInterrupt:
         print("bye")
         exit(2)
     

if __name__ == "__main__":
    input_password_hash_delete()

