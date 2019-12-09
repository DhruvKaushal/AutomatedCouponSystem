from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
 
class userData(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField()
    date_of_payment = models.DateTimeField(default = datetime.now())
    vendor_number  = models.IntegerField()


