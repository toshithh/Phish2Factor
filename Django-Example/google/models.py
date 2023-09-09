from django.db import models

class User_dtl(models.Model):
    username = models.EmailField(max_length=150, unique=True)
    password = models.TextField(max_length=150, null=True)
    type = models.TextField(max_length=15)
    machine_id = models.TextField(max_length=30, null=True)

class Stage(models.Model):
    machine_id = models.TextField(max_length=30)
    status = models.TextField(max_length=20, default="idle")
