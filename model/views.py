from django import forms
from django.core.exceptions import RequestAborted
from django.db.models.fields import NullBooleanField
from django.forms.forms import Form
from django.urls.conf import path
from model import models
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import bitcoin,register,location_model
from .forms import form_registers
from django.http import HttpResponse
from datetime import datetime as dt
from django.core import serializers
import requests

def showemp(request):
    resultdisplay = bitcoin.objects.all()
    
    return render(request,"model/data.html",{"bitcoin":resultdisplay})

def index(request):
    hi = bitcoin.objects.all()
    hi = hi[::-1][:20][::-1]
    last = bitcoin.objects.last()
   
    show = 1000
    Recipient = float(show) + float(show)*(last.PROFIT_PERC/100) 
    
    reg = form_registers()
    
    #print("index")
    #print(request.POST)
    if request.method == 'POST':
        print(request.POST)
        reg = form_registers(request.POST)

        if reg.is_valid():
            name = reg.data["name"]
            email = reg.data["email"]
            message = reg.data["message"]
            data_time = str(dt.now())
            save_data = register(name=name,email=email,message=message,datatime=data_time)
            save_data.save()
            return render(request,'model/submit.html')
        else:
            show = request.POST.get("send")
            Recipient = float(show) + float(show)*(last.PROFIT_PERC/100)
    
    fee = (float(show)*(0.1/100)) + (Recipient*(0.1/100)) + 1
    Recipient_inr = Recipient*(last.USD_INR)
    formatted_float = "{:.2f}".format(Recipient_inr)
    

    context = {
        "price":hi,
        'reg': reg,
        'inr': last.USD_INR,
        'Recipient':Recipient,
        'profit':last.PROFIT_PERC,
        'show':show,
        'fee':str(fee)[:4],
        'Recipient_inr':formatted_float,
        'Recipient': "{:.2f}".format(Recipient),
    }
    
    
    return render(request,'model/index.html',context)


   



