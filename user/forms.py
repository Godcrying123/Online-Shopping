from django import forms
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='E-Mail', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'mail', 'password', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserProfileGetForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('name', 'username', 'mail', 'telephone')


class UserProfileChangeForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100,
                           required=True)
    username = forms.CharField(label='UserName', max_length=100,
                               required=True)
    mail = forms.EmailField(label='E-mail', required=True,
                            max_length=100)
    telephone = forms.CharField(label='Telephone', max_length=100,
                                required=True)
    # recaddress = forms.CharField(label='Recaddress', max_length=100,
    #                              required=True)