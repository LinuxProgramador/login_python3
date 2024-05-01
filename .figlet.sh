#!/bin/bash

usuario=$(cat ~/login_python3/.usuario.txt | base64 -d | cut -f1)
banner_1=$(cat ~/login_python3/.banner.txt | cut -f1)

figlet -f $banner_1 Bienvenido $usuario!
neofetch
