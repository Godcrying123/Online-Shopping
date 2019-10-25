from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View

from .forms import LoginForm, UserRegistrationForm, UserProfileGetForm, UserProfileChangeForm, UserInfoEntityForm
from .models import User, UserInfoEntity
from .tasks import user_registered
from django.core.cache import cache

# from django.contrib.auth import authenticate, login


class LoginView(View):
    template_name = 'user/login.html'

    def get(self, request):
        form = LoginForm()
        print(settings.LOCALE_PATHS[0])
        print(settings.STATICFILES_DIRS[0])
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        response = HttpResponseRedirect(reverse('index_view'))
        context = {
            'form': None,
            'loginresult': None
        }
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            # email = cd['email']
            password = cd['password']
            context['form'] = form
            try:
                instance = User.objects.get(username=username, password=password)
                context['loginresult'] = 'Login Success!'
                response.set_signed_cookie('username', username, salt=settings.COOKIE_SALT_VALUE,
                                           expires=settings.COOKIE_EXPIRE_TIME)
            except User.DoesNotExist:
                try:
                    instance = User.objects.get(username=username)
                    context['loginresult'] = 'Wrong Password!'
                    return render(request, self.template_name, context)
                except User.DoesNotExist:
                    # print(self.context['loginresult'])
                    context['loginresult'] = 'Wrong Username, Email or Password!'
                    return render(request, self.template_name, context)
        return response


class RegistrationView(View):
    template_name = 'user/register.html'

    def get(self, request):
        user_form = UserRegistrationForm()
        username = request.get_signed_cookie('username', default=None, salt=settings.COOKIE_SALT_VALUE,
                                             max_age=settings.COOKIE_EXPIRE_TIME)
        response = render(request, self.template_name, {'user_form': user_form, 'haslogged': username})
        if username is not None:
            response.delete_cookie('username')
        return response

    def post(self, request):
        context = {
            'user_form': None,
            'registrationresult': None
        }
        response = HttpResponseRedirect(reverse('index_view'))
        user_form = UserRegistrationForm(request.POST)
        context['user_form'] = user_form
        if user_form.is_valid():
            cd = user_form.cleaned_data
            username = cd['username']
            email = cd['mail']
            password = user_form.clean_password2()
            try:
                userinstance = User.objects.get(username=username)
                context['registrationresult'] = 'the UserName has been used'
                return render(request, self.template_name, context)
            except User.DoesNotExist:
                try:
                    userinstance = User.objects.get(mail=email)
                    context['registrationresult'] = 'the E-Mail has been used'
                    return render(request, self.template_name, context)
                except User.DoesNotExist:
                    new_user = User.objects.create(username=username, mail=email, password=password)
                    print(new_user.id)
                    # launch asychronous task
                    user_registered.delay(new_user.id)
                    response.set_signed_cookie('username', username, salt=settings.COOKIE_SALT_VALUE,
                                               expires=settings.COOKIE_EXPIRE_TIME)
                    return response


class ProfileView(View):
    template_name = 'user/profile.html'

    def get(self, request, *args, **kwargs):
        username = request.get_signed_cookie('username', default=None, salt=settings.COOKIE_SALT_VALUE,
                                        max_age=settings.COOKIE_EXPIRE_TIME)
        if username is None:
            return redirect(reverse('user:login'))
        userinfoentity = self.request.GET.get('userinfoentity')
        userinstance = get_object_or_404(User, username=username)
        profile_form = UserProfileGetForm(instance=userinstance)
        if userinfoentity is None:
            userinfo_form = UserInfoEntityForm()
            try:
                del request.session['userinfo_id']
            except KeyError:
                pass
        else:
            userinfoentity_instance = get_object_or_404(UserInfoEntity, id=userinfoentity)
            userinfo_form = UserInfoEntityForm(initial={'name': userinfoentity_instance.name,
                                                        'mail': userinfoentity_instance.mail,
                                                        'telephone': userinfoentity_instance.telephone,
                                                        'recaddress': userinfoentity_instance.recaddress,
                                                        'recaddresspostal': userinfoentity_instance.recaddresspostal})
            request.session['userinfo_id'] = userinfoentity
        return render(request, self.template_name, {'profile_form': profile_form, 'userinfo_form': userinfo_form,
                                                    'user': userinstance, 'haslogged': username})

    def post(self, request, *args, **kwargs):
        # context = {
        #     'profile_form': None,
        #     'profilesaveresult': None
        # }
        # context['profile_form'] = profile_form
        profile_form = UserProfileChangeForm(request.POST)
        userid = kwargs.get('pk')
        response = redirect('user:profile_view')
        if profile_form.is_valid():
            cd = profile_form.cleaned_data
            name = cd['name']
            username = cd['username']
            telephone = cd['telephone']
            email = cd['mail']
            userinstance = get_object_or_404(User, pk=userid)
            userinstance.name = name
            userinstance.mail = email
            userinstance.telephone = telephone
            if not userinstance.username == username:
                response.set_signed_cookie('username', username, salt=settings.COOKIE_SALT_VALUE,
                                           expires=settings.COOKIE_EXPIRE_TIME)
            userinstance.save()
        return response


def logout(request):
    response = redirect(reverse('index_view'))
    response.delete_cookie('username')
    return response


class UserInfo(View):
    template_name = 'user/profile.html'

    def post(self, request):
        username = request.get_signed_cookie('username', default=None, salt=settings.COOKIE_SALT_VALUE,
                                        max_age=settings.COOKIE_EXPIRE_TIME)
        if username is None:
            return redirect(reverse('user:login'))
        ownerinstance = get_object_or_404(User, username=username)
        userinfo_form = UserInfoEntityForm(request.POST)
        userinfoentity_id = request.session.get('userinfo_id', None)
        if userinfo_form.is_valid():
            cd = userinfo_form.cleaned_data
            name = cd['name']
            mail = cd['mail']
            telephone = cd['telephone']
            recaddress = cd['recaddress']
            recaddresspostal = cd['recaddresspostal']
            if userinfoentity_id is not None:
                userinfoinstance = get_object_or_404(UserInfoEntity, id=userinfoentity_id)
                userinfoinstance.name = name
                userinfoinstance.mail = mail
                userinfoinstance.telephone = telephone
                userinfoinstance.recaddress = recaddress
                userinfoinstance.recaddresspostal = recaddresspostal
                userinfoinstance.save()
            else:
                newuserinfoinstance = UserInfoEntity.objects.create(owner=ownerinstance, name=name, mail=mail,
                                                                    telephone=telephone, recaddress=recaddress,
                                                                    recaddresspostal=recaddresspostal)
        response = HttpResponseRedirect(reverse('user:profile_view'))
        return response

