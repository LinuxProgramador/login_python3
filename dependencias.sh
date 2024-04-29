#!/bin/bash

echo $(clear)

apt update && apt upgrade -y

apt install figlet python3 nano -y

echo $(clear)


echo -e "\033[1;35mescriba su contraseña y elige un hash para codificarla "
printf "\e[1;37m"

python3 ~/login_python3/hash_pass.py


function input_dates {

   read -p "ingresa tu nombre para agregarlo al banner: " nombre_usuario

   echo "lista de banners en figlet para el login"
   echo -e "\033[1;34m  big.flf"
   echo -e "\033[1;34m  banner.flf"
   echo -e "\033[1;34m  digital.flf"
   echo -e "\033[1;34m  small.flf"
   echo -e "\033[1;34m  slant.flf"
   echo -e "\033[1;34m  shadow.flf"
   echo -e "\033[1;34m  smscript.flf"
   echo -e "\033[1;34m  smslant.flf"
   echo -e "\033[1;34m  block.flf"
   echo -e "\033[1;34m  bubble.flf"
   echo -e "\033[1;37m"

   read -p "elige un banner para tu login: " valores
   echo "listo ya esta todo configurado"
   echo "ejecuta python3 login.py para utilzar el login"
   echo $valores | base64 > ~/login_python3/.banner.txt
   echo $nombre_usuario | base64  > ~/login_python3/.usuario.txt
   chmod +x ~/login_python3/.figlet.sh
}
input_dates
