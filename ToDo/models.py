from django.db import models


class User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    password = models.CharField(null=False, blank=False)
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True)


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=999)
    status = models.CharField(max_length=32)
    due_date = models.DateTimeField
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL
    )
