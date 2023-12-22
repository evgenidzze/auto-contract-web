# auto-contract-web
 
git clone https://github.com/evgenidzze/auto-contract-web

cd .\auto-contract-web\

python3 -m venv venv

source venv\bin\activate

pip install -r .\requirements.txt

#create MySQL db 'auto_contract'

.\db_connect.py

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

chcp 65001 

mysql -u root -p --default-character-set=utf8 auto_contract < pages_so.sql

mysql -u root -p --default-character-set=utf8 auto_contract < pages_department.sql

mysql -u root -p --default-character-set=utf8 auto_contract < pages_consumercategory.sql

python manage.py runserver
