from django import forms
from .models import *


class SalesForm(forms.ModelForm):   
    class Meta:
        models = SaleAnalysis
        fields = '__all__'

class ProfitForm(forms.ModelForm):
    class Meta:
        model = ProfitAnalysis
        fields = '__all__'

class TrxnForm(forms.ModelForm):
    sale_date = forms.ModelChoiceField(queryset=SaleAnalysis.objects.all())
    
    class Meta:
        models = TrxnAnalysis
        fields = '__all__'
