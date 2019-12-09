from django.shortcuts import render
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from .models import userData
# Create your views here.
def adminKaPage(request):
    model = userData
    records = model.objects.all().order_by(model.name)
    return render(request, 'profiles/adminKaLogin.html')
