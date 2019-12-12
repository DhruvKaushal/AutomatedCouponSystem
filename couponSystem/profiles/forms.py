from django import forms
from django.contrib.auth import get_user_model

vendor_choices = [
    ('1','Vendor 1'),('2',"Vendor 2"), ("3", "Vendor 3"),
]    

class select_vendor_form(forms.Form):
    Vendor_choices = forms.ChoiceField(choices=vendor_choices,
                                widget=forms.RadioSelect)
    