from send_mail.celery import app
from .service import send
from .models import Contact
from django.core.mail import send_mail


@app.task
def send_spam_email(user_email):
    send(user_email)


@app.task
def spam():
    for contact in Contact.objects.all():
        send_mail(
            'your subscribe to sending.',
            'We send your more spam.',
            'DjangoTestemail2022@gmail.com',
            [contact.email],
            fail_silently=False,
        )
