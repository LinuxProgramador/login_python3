
cd ~

git clone 

cd login_python3

chmod u+x dependencias.sh login.py hash_pass.py

bash dependencias.sh




Nota: si quieres que se carge el login siempre que abra termux 

copia el ejecutable login.py a binarios

por ejemolo:

cp login.py $PATH

despues 

ve a $PREFIX/etc 

abre el archivo bash.bashrc con nano 

ejemplo: nano bash.bashrc

agrega por arriba de la variable PS1 este comando: python3 $PATH/login.py

despues se te abrira el login cada ves que inicies seccion
