from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View
# from django.contrib.auth import authenticate, login

from .models import Users
from .forms import LoginForm, UserRegistrationForm, UserProfileGetForm, UserProfileChangeForm


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
    template_name = 'user/profile.html'
    useridlist = []

    def userlistchange(self, userid):
        if len(self.useridlist) != 0:
            self.useridlist.clear()
        self.useridlist.append(userid)

    def get(self, request, *args, **kwargs):
        userid = kwargs.get('pk')
        userinstance = get_object_or_404(Users, pk=userid)
        profile_form = UserProfileGetForm(instance=userinstance)
        self.userlistchange(userid)
        return render(request, self.template_name, {'profile_form': profile_form})

    def post(self, request, *args, **kwargs):
        context = {
            'profile_form': None,
            'profilesaveresult': None
        }
        profile_form = UserProfileChangeForm(request.POST)
        context['profile_form'] = profile_form
        userid = self.useridlist[0]
        if profile_form.is_valid():
            cd = profile_form.cleaned_data
            name = cd['name']
            username = cd['username']
            telephone = cd['telephone']
            email = cd['mail']
            userinstance = get_object_or_404(Users, pk=userid)
            recaddress = cd['recaddress']
            userinstance.name = name
            userinstance.username = username
            userinstance.mail = email
            userinstance.telephone = telephone
            userinstance.recaddress = recaddress
            userinstance.save()
        return HttpResponseRedirect('/view/user/profile/'+str(userid)+'/')