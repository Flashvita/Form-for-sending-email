
#Install virtual environment

python3 -m virtualenv venv


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

celery -A send_mail worker -l Info
