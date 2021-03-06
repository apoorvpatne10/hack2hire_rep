# Generated by Django 2.2.3 on 2020-01-18 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0006_rule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rule',
            name='name',
        ),
        migrations.RemoveField(
            model_name='rule',
            name='value',
        ),
        migrations.RemoveField(
            model_name='rule',
            name='weight',
        ),
        migrations.AddField(
            model_name='rule',
            name='charges_electric',
            field=models.CharField(default='charges electric', max_length=150),
        ),
        migrations.AddField(
            model_name='rule',
            name='charges_electric_value',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='rule',
            name='charges_electric_weight',
            field=models.FloatField(default=1.0),
        ),
        migrations.AddField(
            model_name='rule',
            name='penalty_tax',
            field=models.CharField(default='penalty tax', max_length=150),
        ),
        migrations.AddField(
            model_name='rule',
            name='penalty_tax_value',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='rule',
            name='penalty_tax_weight',
            field=models.FloatField(default=1.0),
        ),
        migrations.AddField(
            model_name='rule',
            name='threshold',
            field=models.CharField(default='threshold', max_length=150),
        ),
        migrations.AddField(
            model_name='rule',
            name='threshold_value',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='rule',
            name='threshold_weight',
            field=models.FloatField(default=1.0),
        ),
        migrations.AddField(
            model_name='rule',
            name='traffic_challan',
            field=models.CharField(default='traffic challan', max_length=150),
        ),
        migrations.AddField(
            model_name='rule',
            name='traffic_challan_value',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='rule',
            name='traffic_challan_weight',
            field=models.FloatField(default=1.0),
        ),
        migrations.AddField(
            model_name='rule',
            name='utility_bills',
            field=models.CharField(default='utility bills', max_length=150),
        ),
        migrations.AddField(
            model_name='rule',
            name='utility_bills_value',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='rule',
            name='utility_bills_weight',
            field=models.FloatField(default=1.0),
        ),
    ]
