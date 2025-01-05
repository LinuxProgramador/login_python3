Uso:

    cd ~

    git clone https://github.com/LinuxProgramador/login_python3.git 

    cd login_python3

    chmod u+x dependencias.sh 

    bash dependencias.sh

Eliminar el login:

    bash uninstall.sh


Nota: si quieres que se carge el login siempre que abra termux 

copia el ejecutable login.py a binarios

por ejemolo:

    cp login.py $PATH

despues ve a $PREFIX/etc 

    cd $PREFIX/etc

abre el archivo bash.bashrc con nano 

ejemplo: 
     
    nano bash.bashrc

agrega por arriba de la variable PS1 este comando: python3 $PATH/login.py

despues se te abrira el login cada ves que inicies seccion
