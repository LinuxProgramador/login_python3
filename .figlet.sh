
usuario=$(cat ~/login_python3/.usuario.txt | base64 -d | cut -f1)
banner_1=$(cat ~/login_python3/.banner.txt | base64 -d | cut -f1)
echo -e "\033[1;35m#####################################################################################"
echo -e "\033[1;35m#####################################################################################"
echo -e "\033[1;35m#####################################################################################"
echo -e "\033[1;35m#####################################################################################"
figlet -f $banner_1 Bienvenido $usuario!
echo -e "\033[1;35m#####################################################################################"
echo -e "\033[1;35m#####################################################################################"
echo -e "\033[1;35m#####################################################################################"
echo -e "\033[1;35m#####################################################################################"
