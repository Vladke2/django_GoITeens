# Generated by Django 4.2.16 on 2025-01-30 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_drf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='age',
            field=models.IntegerField(default=15),
            preserve_default=False,
        ),
    ]
