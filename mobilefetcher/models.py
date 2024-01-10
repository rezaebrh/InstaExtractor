from django.db import models

class FetchingAccount(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class InvestigatedAccount(models.Model):
    phonenumber = models.IntegerField(max_length=255)
    password = models.CharField(max_length=255)

