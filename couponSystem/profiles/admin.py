from django.contrib import admin
from .models import vendor, employee, transaction
# Register your models here.
admin.site.register(vendor)
admin.site.register(employee)
admin.site.register(transaction)