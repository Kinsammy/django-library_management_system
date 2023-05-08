from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage, BadHeaderError

from templated_mail.mail import BaseEmailMessage


# Create your views here.
# todo -> for using send_mail() to send maiil
# todo -> either using console or smtp (make sure you configure in settings.py)
def playground(request):
    send_mail('test mail', 'this email is from django',
              '', ['fanusamuel@gmail.com'])
    return HttpResponse("Email sent")


def send_email(request):
    try:
        message = EmailMessage('test mail', 'this email is from django',
                               'admin@gmail.com', ['fanusamuel@gmail.com'])
        message.attach_file('email/static/images/samuel.jpg')
        message.send()
    except BadHeaderError:
        pass
    return HttpResponse("Email sent")


# todo -> send mail with html file
def send_with_template(request):
    try:
        message = BaseEmailMessage(
            template_name='email/greeting.html',
            context={'name': 'Samuel'}
        )
        message.send(['sammy@gmail.com'])
    except BadHeaderError:
        pass
    return HttpResponse("Email sent")
