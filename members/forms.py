from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class RegisterForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')
        
        widgets= {
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter you email'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username '}),
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

