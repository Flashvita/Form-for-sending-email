

#Install virtual environment

python3 -m install venv venv

#Activate

source venv/bin/activate

#Install requirements

pip install django==4.0.0

pip install celery



#Make migrate

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

#Run project

python manage.py runserver

#Run celery

#in other terminal write

celery -A DjangoForm worker -l Info