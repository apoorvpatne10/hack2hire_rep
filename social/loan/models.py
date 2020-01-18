from django.db import models


class User(models.Model):
    # s_no = models.IntegerField(default=2)
    name = models.CharField(max_length=150)
    item = models.CharField(max_length=150)
    value = models.IntegerField()

    def __str__(self):
        return self.name


class Rule(models.Model):
    name = models.CharField(max_length=150)
    value = models.IntegerField()
    weight = models.FloatField()
    
