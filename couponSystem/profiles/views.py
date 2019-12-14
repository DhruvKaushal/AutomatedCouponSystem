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
  # Check if the current method was a POST method
  if request.method=="POST":
    # Initiate the form again, but with post data
    form = select_vendor_form(request.POST)
    if form.is_valid():
      choice = form.cleaned_data['Vendor_choices']
      records = userData.objects.get(Vendor_number = ('choice')).aggregate(Sum('balance'))
      args = {'form': form, 'choice': choice, 'model':records}
      return render(request, 'profiles/useLogin.html', args)

  # Return the normal results, form will display an error message if POST was triggered
  return render(request, 'profiles/userLogin.html', {'form': form})