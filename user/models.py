from django.db import models


class User(models.Model):
    username = models.TextField(null=False, max_length=256)
    age = models.IntegerField(null=True)
    firstname = models.TextField(null=False, max_length=128)
    lastname = models.TextField(null=False, max_length=128)
    