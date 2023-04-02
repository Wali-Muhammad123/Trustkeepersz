from django.db import models
from datetime import datetime
from .utils import COUNTRYCODE_PHONE
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    message=models.TextField()
    date=models.DateField()
    def save(self,*args,**kwargs):
        self.date=datetime.now()
        super().save(*args,**kwargs)
class BookMeeting(models.Model):
    #Country Code Options
    COUNTRYCODE_PHONE=COUNTRYCODE_PHONE
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    message=models.TextField(default="")
    countrycode=models.CharField(max_length=5,choices=COUNTRYCODE_PHONE, default=None)
    phone=models.CharField(max_length=15,default="")
    def save(self,*args,**kwargs):
        self.date=datetime.now()
        super().save(*args,**kwargs)