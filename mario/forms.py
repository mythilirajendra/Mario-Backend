from django import forms
from django.contrib.auth.models import User
from .models import CustomUser


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    # email = forms.EmailField(widget=forms.TextInput(attrs={'id': 'input-box', 'placeholder': 'Email'}), label='',
    #                          validators=[validators.EmailValidator])
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'input-box', 'placeholder': 'Password'}),
    #                            label='')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')



