from django.db import models

# Create your models here.
class GoogleAccounts(models.Model):
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
