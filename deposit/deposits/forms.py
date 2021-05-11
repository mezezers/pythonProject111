# import form class from django
from django import forms

from .models import Deposit


# create a ModelForm
class DepositAddForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Deposit
        fields = ['deposit', 'term', 'rate']