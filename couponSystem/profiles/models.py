from django.db import models
from django.contrib.auth.models import User
import django
import datetime
# Create your models here.



class vendor(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=30)

class employee(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.CharField(max_length=20, primary_key=True)
    balance = models.IntegerField(default=0)

class transaction(models.Model):
    vendor_id = models.ForeignKey(vendor, on_delete=models.CASCADE)
    emp_id = models.ForeignKey(employee, on_delete=models.CASCADE)
    debit = models.IntegerField()
    credit = models.IntegerField()
    timestamp = models.DateField(("Date"), default=datetime.date.today)