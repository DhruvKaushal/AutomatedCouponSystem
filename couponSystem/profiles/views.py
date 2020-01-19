from django.shortcuts import render
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
#from .forms import select_vendor_form
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
import datetime

# from django.forms.models import model_to_dict
from .models import vendor, employee, transaction
#from . import forms
# Create your views here.
def adminKaPage(request):
    if request.method=="POST":
        if 'form1' in request.POST:
            d={}
            vendor_choice = request.POST["inlineDefaultRadiosExample"]
            date_choice = request.POST["inlineDefaultRadiosExample1"]
            x = employee.objects.all()
            y = vendor.objects.all()
            if date_choice == 1:
                d = transaction.objects.filter(vendor_id=y, emp_id = x, timestamp__gte = datetime.date.today() - datetime.timedelta(days=30))
            elif date_choice == 1:
                d = transaction.objects.filter(vendor_id=y, emp_id = x, timestamp__gte = datetime.date.today() - datetime.timedelta(days=60))
            else:
                d = transaction.objects.filter(vendor_id=y, emp_id = x, timestamp__gte = datetime.date.today() - datetime.timedelta(days=180))    
            print(d)
            return render(request, 'profiles/adminKaLogin.html', {'model':d})        


        if 'form2' in request.POST:
            amount = request.POST["amt"]
            x = employee.objects.all()
            for i in x:
                i.balance = i.balance + int(amount)
                i.save()
                print(i.id)
                transaction.objects.create(emp_id=i,debit=0,credit=amount)

            return render(request, 'profiles/adminKaLogin.html')

    return render(request, 'profiles/adminKaLogin.html')

def updatingBalance(request):
    if request.method=="POST":
        if 'form1' in request.POST:
            ven_id = request.POST["groupOfDefaultRadios"]
            amount = request.POST["amt"]
            x = employee.objects.get(name = request.user)
            x.balance = x.balance - int(amount)
            x.save()
            v = vendor.objects.get(id=ven_id)
            w = employee.objects.get(id=x.id)
            transaction.objects.create(vendor_id = v, emp_id=w,debit=amount,credit=0)
            y = employee.objects.get(name = request.user)
            return render(request, 'profiles/userLogin.html', {'model':y})

        if 'form2' in request.POST:
            d = {}
            date_id = request.POST["groupOfDefaultRadios1"]
            x = employee.objects.get(name = request.user)
            if date_id == 1:
                d = transaction.objects.filter(emp_id = x, timestamp__gte = datetime.date.today() - datetime.timedelta(days=30))
            elif date_id == 2:
                d = transaction.objects.filter(emp_id = x, timestamp__gte = datetime.date.today() - datetime.timedelta(days=60))
            else:
                d = transaction.objects.filter(emp_id = x, timestamp__gte = datetime.date.today() - datetime.timedelta(days=180))
                print(d)

            return render(request, 'profiles/userLogin.html', {'model':d})    

    return render(request, 'profiles/userLogin.html')



# def userKaLog(request):
#   form = select_vendor_form()
#   # Check if the current method was a POST method
#   if request.method=="POST":
#     # Initiate the form again, but with post data
#     form = select_vendor_form(request.POST)
#     if form.is_valid():
#       choice = form.cleaned_data['Vendor_choices']
#       records = userData.objects.filter(vendor_number = choice, name = User.username)
#       args = {'form': form, 'choice': choice, 'model': records}
#       return render(request, 'profiles/userLogin.html', args)

#   # Return the normal results, form will display an error message if POST was triggered
#   return render(request, 'profiles/userLogin.html', {'form': form})