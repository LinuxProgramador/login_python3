#!/bin/bash



function input_dates_user {

   trap ctrl_c 2

   function ctrl_c() {

       echo $(clear)
       echo "Bye"
       exit

   }


   echo -e "\033[1;35m"
   read -p "Ingresa tu nombre para agregarlo a la configuracion del banner: " user_name
   echo -e "\033[1;35m -------------------------------------------"
   echo -e "\033[1;35m| Lista de banners en figlet para el login  |"
   echo -e "\033[1;35m -------------------------------------------"
   echo -e "\033[1;34m|  big.flf      |"
   echo -e "\033[1;34m|  banner.flf   |"
   echo -e "\033[1;34m|  digital.flf  |"
   echo -e "\033[1;34m|  small.flf    |"
   echo -e "\033[1;34m|  slant.flf    |"
   echo -e "\033[1;34m|  shadow.flf   |"
   echo -e "\033[1;34m|  smscript.flf |"
   echo -e "\033[1;34m|  smslant.flf  |"
   echo -e "\033[1;34m|  block.flf    |"
   echo -e "\033[1;34m|  bubble.flf   |"
   echo -e "\033[1;35m --------------- "
   read -p "Elige un banner para tu login: " user_banner
   echo -e "\033[1;37m"
   echo "listo ya esta todo configurado"
   echo "ejecuta python3 login.py para utilzar el login"
   sleep 3
   echo $user_banner > ~/login_python3/.banner.txt
   echo $user_name | base64  > ~/login_python3/.usuario.txt
   chmod 700 ~/login_python3/.figlet.sh hash_pass.py login.py dependencias.sh
   chmod 600 ~/login_python3/.banner.txt ~/login_python3/.hash_selection.txt ~/login_python3/.password_user.txt ~/login_python3/.usuario.txt ~/login_python3/uninstall.sh ~/login_python3/.hash_uninstall.py ~/login_python3/.password_hash_uninstall.txt ~/login_python3/motd LICENSE README.md motd1

}



function main {

   motd="motd"
   verification_motd=$(cd $PREFIX/etc; ls | grep motd*$ | cut -d'-' -f1)

   echo $(clear)

   apt update && apt upgrade -y

   apt install figlet python3 nano neofetch -y

   if [ "$motd" = "$verification_motd" ]; then

      rm -f $PREFIX/etc/motd
      cp -f ~/login_python3/motd1  $PREFIX/etc/
      echo $(clear)
   else

    echo $(clear)

   fi

   echo -e "\033[1;35m -------------------------------------------------------"
   echo -e "\033[1;35m| Hola por favor digite su contrasena y hash a utilizar |"
   echo -e "\033[1;35m ------------------------------------------------------- "
   sleep 3
   echo $(clear)
   python3 ~/login_python3/hash_pass.py
   input_dates_user
   python3 login.py

}
main


