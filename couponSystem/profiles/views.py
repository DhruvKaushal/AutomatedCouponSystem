from django.shortcuts import render
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from .forms import select_vendor_form
from django.db.models import Sum

# from django.forms.models import model_to_dict
from .models import userData
from . import forms
# Create your views here.
def adminKaPage(request):
    records = userData.objects.all()
    return render(request, 'profiles/adminKaLogin.html',{'model':records})


# def userKaLog(request):
#     form  = select_vendor_form()
#     return render(request, 'profiles/userLogin.html', {'form': form})

def userKaLog(request):
    form = select_vendor_form()
    if request.method=="POST" and form.is_valid():
        choice = form.cleaned_data['Vendor_choices']
        print(choice)
        records = userData.objects.filter(Vendor_number = ('choice')).aggregate(Sum('itemPrice'))
        args = {'form': form, 'choice': choice, 'model':records}
        return render(request, 'profiles/useLogin.html', args)
    else:
        return render(request, 'profiles/userLogin.html', {'form': form})