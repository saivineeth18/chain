from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import  index,showemp


urlpatterns = [
    path("data",showemp,name="showemp"),
    path("",index,name="index"),

   
]

