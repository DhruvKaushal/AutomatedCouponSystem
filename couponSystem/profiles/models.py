from django.db import models
from datetime import datetime
# Create your models here.
 
class userData(models.Model):
    name = models.CharField(max_length=30, on_delete=models.CASCADE)
    balance = models.IntegerField()
    date_of_payment = models.DateTimeField(default = datetime.now())
    vendor_number  = models.
