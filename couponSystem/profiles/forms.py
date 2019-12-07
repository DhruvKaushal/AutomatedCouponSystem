from django import forms
from django.contrib.auth import get_user_model

vendor_choices = [
    ('Vendor 1'), ('Vendor 2'), ('Vendor 3'),
]    

class select_vendor_form(forms.Form):
    vendor = forms.CharField(label='Select the desired vendor', widget = forms.RadioSelect(choices=vendor_choices))
    