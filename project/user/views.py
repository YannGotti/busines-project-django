from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.views.generic.base import View
from .models import CustomUser
import random

class RegisterUser(View):
    def post(self, request):
        data = request.POST

        if (CustomUser.objects.filter(email = data.get("email"))):
            return HttpResponse('Not')
        
        user = CustomUser(username = data.get('email'), email = data.get('email'), userPlaceOfStudy = data.get('userPlaceOfStudy'), password = data.get('password'),
                        type_user = data.get('type_user'), fullName= data.get('fullName'))
        user.set_password(data.get('password'))
        user.save()

        return HttpResponse('Ok')
