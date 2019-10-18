from celery import task
from django.core.mail import send_mail
from .models import User


@task
def user_registered(user_id):
    """
    Task to send an e-mail notification when user is sucessfully registered
    """
    user = User.objects.get(pk=user_id)
    subject = 'Congrations!! Your User Number is {}.'.format(user.id)
    message = 'Dear {}, \n\nYou have successfully registered as a user in this website.\
               Enjoy your shopping in this website'.format(user.username)
    mail_sent = send_mail(subject, message, 'admin@shopsite.com', [user.mail])
    return mail_sent
