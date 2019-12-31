from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required' : 'Please enter your valid username'                    
        }, 
        max_length=32, label="Username")
    password = forms.CharField(
        error_messages={
            'required' : 'Please enter your valid password'                    
        }, 
        widget=forms.PasswordInput, label="Password")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                fcuser = Fcuser.objects.get(username=username)
            except Fcuser.DoesNotExist:
                self.add_error('username', 'We have no such username.')
                return 
            if not check_password(password, fcuser.password):
                self.add_error('password', 'Your password is wrong')
            else:
                self.user_id = fcuser.id