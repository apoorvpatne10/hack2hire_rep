# Generated by Django 2.2.3 on 2020-01-18 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]