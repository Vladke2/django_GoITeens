from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=100)
    about_me = models.CharField(max_length=100)
    created_date = models.DateField()
    age = models.IntegerField()

    def __str__(self):
        return self.name

