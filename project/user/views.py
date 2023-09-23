from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.views.generic.base import View
from .models import CustomUser
from django.template.loader import render_to_string 
from django.contrib.sites.shortcuts import get_current_site 
from django.utils.encoding import force_bytes, force_str 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from .tokens import account_activation_token

from .smtp import SMTPServer

class RegisterUser(View):
    def post(self, request):
        data = request.POST

        if (CustomUser.objects.filter(email = data.get("email"))):
            return HttpResponse('Not')
        
        user = CustomUser(username = data.get('email'), email = data.get('email'), userPlaceOfStudy = data.get('userPlaceOfStudy'), password = data.get('password'),
                        type_user = data.get('type_user'), fullName= data.get('fullName'))
        user.is_active = False
        user.set_password(data.get('password'))
        user.save()

        current_site = get_current_site(request) 

        smtp_server = SMTPServer()
        smtp_server.send_message(f'Ваша учетная запись - {user.username}. АКТИВАЦИЯ АККАУНТА', GenerateMail(user, current_site), user.email, html_content = None)


        return HttpResponse('Ok')
    

class ActivateValidate(View):
    def get(self, request): 
        data = request.GET
        uidb64 = data.get('uidb64')
        token = data.get('token')

        User = CustomUser
        try: 
            uid = force_str(urlsafe_base64_decode(uidb64)) 
            user = User.objects.get(pk=uid) 
        except(TypeError, ValueError, OverflowError, User.DoesNotExist): 
            user = None 
        if user is not None and account_activation_token.check_token(user, token): 
            user.is_active = True 
            user.save() 
            return HttpResponse('Вы успешно активировали аккаунт!') 
        else: 
            return HttpResponse('Непредвиденная ошибка!') 


def GenerateMail(user, current_site):
    message = f"<p>Привет {user.username}</p><p>Для завершения регистрации нажми на ссылку:</p><p>{current_site.domain}/auth/activate/account/?uidb64={urlsafe_base64_encode(force_bytes(user.pk))}&token={account_activation_token.make_token(user)}</p>"
    
    return message
