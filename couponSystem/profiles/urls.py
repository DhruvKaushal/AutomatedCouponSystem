from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'profiles'

urlpatterns = [
    path('adminKaLogin/', views.adminKaPage, name="adminHome"),
    path('userLogin/', views.updatingBalance, name="userHome"),
]
