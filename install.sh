echo "Iniciando  instalação"
sleep 1 
pkg install python -y 
clear
pip install colorama 
clear
pip install tqdm 
clear
pip install scapy
clear
echo "Instalação completa"
var1="1"
echo "Iniciar script"
echo "1) Sim"
echo "2) Não"
read -p ">> " resp
if [ "$resp" == "$var1" ]
then
python3 mavis.py
else