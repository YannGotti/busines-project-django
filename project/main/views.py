import os
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import View
from django.core.files.storage import FileSystemStorage
from user.models import CustomUser, Questionnaire, Project
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
        project = None

        if (request.user.type_user == 'Предприниматель'):
            try:
                project = Project.objects.filter(user = request.user)
            except :
                return render(request, 'main/profile.html', context={'user_data': request.user})
            
            return render(request, 'main/profile.html', context={'project' : project , 'user_data': request.user})
        
        else:
            try:
                questionnaire = Questionnaire.objects.get(user = request.user)
            except :
                return render(request, 'main/profile.html', context={'user_data': request.user})
        
            return render(request, 'main/profile.html', context={'questionnaire' : questionnaire , 'user_data': request.user})



    
class ProfileUserPage(View):
    def get(self, request, pk):
        
        questionnaire = None
        project = None
        user = None

        try:
            user = CustomUser.objects.get(id = pk)
        except:
            return render(request, 'main/profile.html')


        if (user.type_user == 'Предприниматель'):
            try:
                project = Project.objects.filter(user = user)
            except :
                return render(request, 'main/profile.html', context={'user_data': user})
            
            return render(request, 'main/profile.html', context={'project' : project , 'user_data': user})
        
        else:
            try:
                questionnaire = Questionnaire.objects.get(user = user)
            except :
                return render(request, 'main/profile.html', context={'user_data': user})
        
            return render(request, 'main/profile.html', context={'questionnaire' : questionnaire , 'user_data': user})

    
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
        questionnaires = Questionnaire.objects.all()

        context = {
            'questionnaires' : questionnaires
        }

        return render(request, 'main/questionnaires.html', context=context)
    

class QuestionnairesFilter(View):
    def get(self, request):
        questionnaires = Questionnaire.objects.filter(areaOfWork = request.GET.get('filter'))


        data = list(questionnaires.values())

        data = {
            'type_user' : request.user.type_user,
            'data' : data
        }

        return JsonResponse(data, safe=False)
    

class PublicProject(View):
    def post(self, request):
        data = request.POST

        nameProject = data.get('nameProject')
        waitSolary = data.get('waitSolary')
        description = data.get('description')
        list_skill = data.get('list_skill')
        list_task = data.get('list_task')
        posts = data.getlist('posts[]')

        id_user = data.get('id')
        user = CustomUser.objects.get(id = id_user)

        posts_string = ''
        for post in posts:
            posts_string += f'{post};'

        project = Project(
            nameProject = nameProject,
            waitSolary = waitSolary,
            description = description,
            list_skill = list_skill,
            list_task = list_task,
            posts = posts_string,
            user = user
        )

        project.save()
        return JsonResponse("ok", safe=False)
    

class ProjectsPage(View):
    def get(self, request):
        projects = Project.objects.all()

        context = {
            'projects' : projects
        }

        return render(request, 'main/projects.html', context=context)