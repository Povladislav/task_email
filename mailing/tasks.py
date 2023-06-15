from celery import shared_task
from django.core.mail import send_mail
from .models import MailingList


@shared_task
def send_mailing(mailing_list_id, subject, message):
    mailing_list = MailingList.objects.get(id=mailing_list_id)
    recipient = mailing_list.email
    send_mail(subject, message, 'sender@example.com', [recipient])
