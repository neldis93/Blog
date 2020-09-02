from django import forms
from django.contrib.auth import authenticate
#
from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}
        )
    )
    password2 = forms.CharField(
        label='Repeat Password',
        required=True,
        widget=forms.PasswordInput(
        attrs={'placeholder': 'Repeat Password'}
        )
    )

    class Meta:
        model = User
        fields = (
            'email',
            'full_name',
            'ocupation',
            'gender',
            'date_birth',
        )
        widgets= {
            'email': forms.EmailInput(
                attrs={'placeholder':'Enter Email'}
                ),
            'full_name': forms.TextInput(
                attrs={'placeholder': 'Name'}
                ),
            'ocupation': forms.TextInput(
                attrs={'placeholder':'Ocupation'}
                ),
            'date_birth': forms.DateInput(
                attrs={'type': 'date'}  
                ),
        }
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Password are not the same')


class LoginForm(forms.Form):
    email = forms.CharField(
        label='E-mail',
        required=True,
        widget=forms.TextInput(
        attrs={'placeholder': 'Email',}
        )
    )
    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('User data is not correct')
        
        return self.cleaned_data


class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
        attrs={'placeholder': 'Current Password'}
        )
    )
    password2 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
        attrs={'placeholder': 'New password'}
        )
    )