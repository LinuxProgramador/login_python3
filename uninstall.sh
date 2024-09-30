#!/bin/bash

login="$PATH/login.py"

function uninstall_login_termux {
 if [ -f "$login" ] ; then
     rm -f $PATH/login.py
     echo "El archivo login.py a sido eliminado con exito de la ruta: $PATH"
     sleep 5
     echo $(clear)
 else
     echo "No existe el archivo login.py en la ruta: $PATH"
     sleep 5
     echo $(clear)
 fi
 mv ~/login_python3/motd  /data/data/com.termux/files/usr/etc/motd
 echo "Se restablecio el archivo motd a su nombre por defecto en la ruta: $PREFIX/etc"
 sleep 5
 echo $(clear)
 cd ~
 rm -rf ~/login_python3
 cd ~
 echo "Se borro el directorio login_python3 del directorio HOME"
 echo "NOTA:si configuraste el bash.bashrc para cargar el script login termux"
 echo ""
 echo "Tienes que seguir estos pasos para desactivarlo"
 echo ""
 echo "cd $PREFIX/etc"
 echo "nano bash.bashrc"
 echo "Borra en donde dice: python3 PATH/login.py"
}

function main {
 trap "echo $(clear) && echo 'Bye' && exit" 2
 read -p "Desea eliminar login termux (si/no): " delete_login_termux
 if [ "$delete_login_termux" = 'si' ] ; then
       secure_token=$(python3 ~/login_python3/.hash_uninstall.py)
       secure_token_input=$(cat ~/login_python3/.password_hash_uninstall.txt | cut -f1)
       if [ "$secure_token" = "$secure_token_input"  ] ; then
               uninstall_login_termux
       else
             echo "Contraseña invalida"
             exit
       fi
 else
      echo "Operacion cancelada"
 fi
}
main
