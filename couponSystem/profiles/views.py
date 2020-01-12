from django.shortcuts import render
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
#from .forms import select_vendor_form
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# from django.forms.models import model_to_dict
from .models import vendor, employee, transaction
#from . import forms
# Create your views here.
def adminKaPage(request):
    records = transaction.objects.all()
    return render(request, 'profiles/adminKaLogin.html',{'model':records})

def updatingBalance(request):
    if request.method=="POST":
        ven_id = request.POST["defaultRadios"]
        amount = request.POST["amt"]
        x = employee.objects.filter(id = request.User.id)
        x.balance = x.balance - amount
        p = transaction(vendor_id =ven_id.value, emp_id = request.User.id, debit=amount, credit=0)
        p.save()
        y = employee.objects.filter(id = request.User.id)
        return render(request, 'profiles/userLogin.html', {'model':y})

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



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