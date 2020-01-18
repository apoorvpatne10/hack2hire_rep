from django.db import models


class User(models.Model):
    name = models.CharField(max_length=150)
    item = models.CharField(max_length=150)
    value = models.IntegerField()

    def __str__(self):
        return self.name


class MyUser(models.Model):
    uid = models.IntegerField()
    uname = models.CharField(max_length=150)
    score = models.FloatField()
    email = models.EmailField(default='abc@gmail.com')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.uname



class Rule(models.Model):
    utility_bills = models.CharField(max_length=150, default='utility bills')
    utility_bills_value = models.IntegerField(default=1)
    utility_bills_weight = models.FloatField(default=1.0)

    traffic_challan = models.CharField(max_length=150, default='traffic challan')
    traffic_challan_value = models.IntegerField(default=1)
    traffic_challan_weight = models.FloatField(default=1.0)

    charges_electric = models.CharField(max_length=150, default='charges electric')
    charges_electric_value = models.IntegerField(default=1)
    charges_electric_weight = models.FloatField(default=1.0)

    penalty_tax = models.CharField(max_length=150, default='penalty tax')
    penalty_tax_value = models.IntegerField(default=1)
    penalty_tax_weight = models.FloatField(default=1.0)

    threshold = models.CharField(max_length=150, default='threshold')
    threshold_value = models.IntegerField(default=1)
    threshold_weight = models.FloatField(default=1.0)

    # def __str__(self):
    #     return self.name
