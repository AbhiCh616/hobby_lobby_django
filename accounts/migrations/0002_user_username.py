# Generated by Django 3.1.6 on 2021-02-03 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=None, max_length=30, unique=True),
        ),
    ]
