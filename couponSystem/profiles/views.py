from django.shortcuts import render
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
# from django.forms.models import model_to_dict
from .models import userData
from . import forms
# Create your views here.
def adminKaPage(request):
    records = userData.objects.all()
    return render(request, 'profiles/adminKaLogin.html',{'model':records})


def userKaLog(request):
    return render(request, 'profiles/userLogin.html')