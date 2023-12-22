# auto-contract-web
 
git clone https://github.com/evgenidzze/auto-contract-web

cd .\auto-contract-web\

sudo /usr/local/bin/python3.10 -m venv appenv 

source appenv/bin/activate 

pip install -r requirements.txt

#create MySQL db 'auto_contract'

python3.10 db_connect.py

python3.10 manage.py makemigrations

python3.10 manage.py migrate

python3.10 manage.py createsuperuser

chcp 65001 

mysql -u root -p --default-character-set=utf8 auto_contract < pages_so.sql

mysql -u root -p --default-character-set=utf8 auto_contract < pages_department.sql

mysql -u root -p --default-character-set=utf8 auto_contract < pages_consumercategory.sql

python3.10 manage.py runserver
