from django import forms
from django.utils.translation import gettext_lazy as _

from parler.forms import TranslatableModelForm

from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(label=_('Username'), max_length=100)
    # email = forms.EmailField(label='E-Mail', max_length=100)
    password = forms.CharField(label=_('password'), widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label=_('Password'),
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Repeat password'),
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
    name = forms.CharField(label=_('Name'), max_length=100,
                           required=True)
    username = forms.CharField(label=_('UserName'), max_length=100,
                               required=True)
    mail = forms.EmailField(label=_('E-mail'), required=True,
                            max_length=100)
    telephone = forms.CharField(label=_('Telephone'), max_length=100,
                                required=True)
    # recaddress = forms.CharField(label='Recaddress', max_length=100,
    #                              required=True)
