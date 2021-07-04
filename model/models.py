from django import db
from django.db import models,connections
from django.db.models.base import Model
from django.db.models.fields import EmailField
from django.forms import ModelForm

class bitcoin(models.Model):
    BTC_BUSD  = models.FloatField()
    USD_INR = models.FloatField()
    WRX_BTC_INR = models.FloatField()
    BIN_BTC_INR = models.FloatField()
    PROFIT_BTCINR = models.FloatField()
    PROFIT_PERC = models.FloatField()
    datetime_ist = models.DateField()
    time = models.TimeField()
    class Meta:
        db_table="price"

class register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    datatime = models.TextField()
    class Meta:
        db_table="register"




