from time import sleep
from django.core.mail import send_mail
from celery import shared_task
from mobilefetcher.models import FetchingAccount
from mobilefetcher.models import InvestigatedAccount

@shared_task()
def find_username():
    all_fetching_accounts = FetchingAccount.objects.all()
    all_investigating_accounts = InvestigatedAccount.objects.all()