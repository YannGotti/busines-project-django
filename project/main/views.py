import os
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import View
from django.core.files.storage import FileSystemStorage
from user.models import CustomUser, Questionnaire
from django.core.exceptions import ObjectDoesNotExist
import json

class MainPage(View):
    def get(self, request):
        return render(request, 'main/index.html')
    

class AuthPage(View):
    def get(self, request):
        return render(request, 'main/auth.html')
    
class ProfilePage(View):
    def get(self, request):

        if (not request.user.id):
            return render(request, 'main/profile.html')
        
        questionnaire = None

        try:
            questionnaire = Questionnaire.objects.get(user = request.user)
        except :
            return render(request, 'main/profile.html')


        return render(request, 'main/profile.html', context={'questionnaire' : questionnaire})

    
class UploadPhotoProfile(View):
    def post(self, request):
        if request.method == 'POST' and request.FILES['file']:
            data = request.POST
            filename = ''
            image = request.FILES['file']

            fss = FileSystemStorage(location='media/photo_profile/')

            file = fss.save(image.name, image)
            id_user = request.POST.get('id')
            user = CustomUser.objects.get(id = id_user)

            if os.path.isfile(f'media/photo_profile/{user.photo_profile}'):
                os.remove(f'media/photo_profile/{user.photo_profile}')

            user.photo_profile = file
            user.save()
            return JsonResponse("ok", safe=False)
        

class SendQuestionnaire(View):
    def post(self, request):
        if request.method != 'POST':
            return JsonResponse("Not", safe=False)

        data = request.POST

        user = CustomUser.objects.get(id = data.get('id'))
        new_work = data.get('new_work')
        areaOfWork = data.get('areaOfWork')
        old_work = data.get('old_work')
        experience = data.get('experience')
        freework = json.loads(data.get('freework'))
        salary = data.get('salary')

        if (freework): salary = 0

        questionnaire = Questionnaire(
            new_work = new_work,
            areaOfWork = areaOfWork, 
            old_work = old_work, 
            experience = experience , 
            freework = freework, 
            salary = salary, 
            user = user
        )
        
        questionnaire.save()

        return JsonResponse("ok", safe=False)
    

class QuestionnairesPage(View):
    def get(self, request):
        return render(request, 'main/questionnaires.html')