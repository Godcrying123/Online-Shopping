from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
# from django.contrib.auth import authenticate, login

from .models import Users
from .forms import LoginForm, UserRegistrationForm, UserProfileForm


class LoginView(View):
    template_name = 'user/login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        context = {
            'form': None,
            'loginresult': None
        }
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            email = cd['email']
            password = cd['password']
            context['form'] = form
            try:
                instance = Users.objects.get(username=username, mail=email, password=password)
                context['loginresult'] = 'Login Success!'
            except Users.DoesNotExist:
                try:
                    instance = Users.objects.get(username=username, mail=email)
                    context['loginresult'] = 'Wrong Password!'
                    return render(request, self.template_name, context)
                except Users.DoesNotExist:
                    # print(self.context['loginresult'])
                    context['loginresult'] = 'Wrong Username, Email or Password!'
                    return render(request, self.template_name, context)
        return HttpResponseRedirect('/view/')


class RegistrationView(View):
    template_name = 'user/register.html'

    def get(self, request):
        user_form = UserRegistrationForm()
        return render(request, self.template_name, {'user_form': user_form})

    def post(self, request):
        context = {
            'user_form': None,
            'registrationresult': None
        }
        user_form = UserRegistrationForm(request.POST)
        context['user_form'] = user_form
        if user_form.is_valid():
            cd = user_form.cleaned_data
            username = cd['username']
            email = cd['mail']
            password = user_form.clean_password2()
            try:
                userinstance = Users.objects.get(username=username)
                context['registrationresult'] = 'the UserName has been used'
                return render(request, self.template_name, context)
            except Users.DoesNotExist:
                try:
                    userinstance = Users.objects.get(mail=email)
                    context['registrationresult'] = 'the E-Mail has been used'
                    return render(request, self.template_name, context)
                except Users.DoesNotExist:
                    new_user = Users(username=username, mail=email, password=password)
                    new_user.save()
                    return HttpResponseRedirect('/view/')


class ProfileView(View):
    template_name='user/profile.html'

    def get(self, request):
        profile_form = UserProfileForm()
        return render(request, self.template_name,{'profile_form': profile_form})

    def put(self, request):
        profile_form = UserProfileForm(request.POST)
        return render(request, self.template_name,{'profile_form':profile_form})
