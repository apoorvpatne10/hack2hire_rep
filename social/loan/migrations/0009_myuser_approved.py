# Generated by Django 2.2.3 on 2020-01-18 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0008_myuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
