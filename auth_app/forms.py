from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .models import CustomUser

"""
class SigninForm(forms.Form):
    email = forms.CharField(label='email', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
"""
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        #integrate with signup design
        self.fields['password1'].widget.attrs['placeholder'] = 'Set password'
        self.fields['password1'].widget.attrs['class'] = 'input100'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
        self.fields['password2'].widget.attrs['class'] = 'input100'
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class': 'input100', 'type': 'text', 'name': 'username', 'placeholder': 'what is your email?'}))
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)

class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kargs):
        super(PasswordResetForm, self).__init__(*args, **kargs)
        #integrate with signup design
        self.fields['email'].widget.attrs['class'] = 'input100'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)
