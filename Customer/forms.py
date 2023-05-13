from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm, UsernameField
from bootstrap_daterangepicker import widgets, fields

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone']
        # field_classes = {"username": UsernameField}
        # widgets = {
        #     'password': forms.PasswordInput(),
        #     'c_password': forms.PasswordInput(),
        # }

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     c_password = cleaned_data.get('c_password')
    #     if password != c_password:
    #         raise forms.ValidationError('Passwords do not match')


class LoginForm(forms.Form):
    u_email = models.EmailField(max_length=50, null=True)
    password = forms.CharField(widget=forms.PasswordInput)

class CustomerDashboardForm(forms.Form):
    class Meta:
        model = CustomerDashboard
        fields = "__all__"
        # ['username', 'date', 'time', 'date_time']
        widgets = {
            "date": forms.DateInput(),
            "time": forms.TimeInput(),
            "date_time":forms.DateTimeInput(),
        }


class RewardAdminForm(forms.ModelForm):
    points = forms.IntegerField(min_value=1)

    class Meta:
        model = Reward
        fields = ('username', 'points')

    def save(self, commit=True):
        reward = super().save(commit=False)
        reward.points_required = self.cleaned_data['points']
        if commit:
            reward.save()
        return reward
