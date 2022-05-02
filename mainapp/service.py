from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'your subscribe to sending.',
        'We send your more spam.',
        'DjangoTestemail2022@gmail.com',
        [user_email],
        fail_silently=False,
    )
