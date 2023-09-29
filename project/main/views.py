import os
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import View
from django.core.files.storage import FileSystemStorage
from user.models import CustomUser, Questionnaire, Project, Notification
from user.smtp import SMTPServer

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

        me_notifications = Notification.objects.filter(recipient=request.user, state='Archive')
        answer_notifications = Notification.objects.filter(sender=request.user, state='Archive')


        if (request.user.type_user == 'Предприниматель'):
            try:
                project = Project.objects.filter(user = request.user)
            except :
                return render(request, 'main/profile.html', context={'user_data': request.user, 'me_notifications': me_notifications, 'answer_notifications':answer_notifications})
            
            return render(request, 'main/profile.html', context={'project' : project , 'user_data': request.user, 'me_notifications': me_notifications, 'answer_notifications':answer_notifications})
        
        else:
            try:
                questionnaire = Questionnaire.objects.get(user = request.user)
            except :
                return render(request, 'main/profile.html', context={'user_data': request.user, 'me_notifications': me_notifications, 'answer_notifications':answer_notifications})
        
            return render(request, 'main/profile.html', context={'questionnaire' : questionnaire , 'user_data': request.user, 'me_notifications': me_notifications, 'answer_notifications':answer_notifications})



    
class ProfileUserPage(View):
    def get(self, request, pk):
        
        questionnaire = None
        project = None
        user = None
        

        try:
            user = CustomUser.objects.get(id = pk)
        except:
            return render(request, 'main/profile.html')

        me_notifications = Notification.objects.filter(recipient=user, state='Archive')
        answer_notifications = Notification.objects.filter(sender=user, state='Archive')


        if (user.type_user == 'Предприниматель'):
            try:
                project = Project.objects.filter(user = user)
            except :
                return render(request, 'main/profile.html', context={'user_data': user, 'me_notifications': me_notifications, 'answer_notifications':answer_notifications})
            
            return render(request, 'main/profile.html', context={'project' : project , 'user_data': user, 'me_notifications': me_notifications, 'answer_notifications':answer_notifications})
        
        else:
            try:
                questionnaire = Questionnaire.objects.get(user = user)
            except :
                return render(request, 'main/profile.html', context={'user_data': user, 'me_notifications': me_notifications, 'answer_notifications':answer_notifications})
        
            return render(request, 'main/profile.html', context={'questionnaire' : questionnaire , 'user_data': user, 'me_notifications': me_notifications, 'answer_notifications':answer_notifications})

    
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
    

class Application(View):
    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user, state='Active')
        return render(request, 'main/applications.html', context={'notifications' : notifications})
    

class SendApplication(View):
    def post(self, request):

        data = request.POST

        message = data.get('message')
        number_phone = data.get('number_phone')
        recipient_id = data.get('recipient_id')
        sender_id = data.get('sender_id')
        project_id = data.get('project_id')
        project = None

        if (project_id):
            project = Project.objects.get(id=project_id)


        recipient = CustomUser.objects.get(id=recipient_id)
        sender = CustomUser.objects.get(id=sender_id)

        notification = Notification(message=message, number_phone=number_phone, recipient=recipient, sender=sender, project=project)
        notification.save()

        return JsonResponse("ok", safe=False)
    


class SubmitApplication(View):
    def post(self, request):
        data = request.POST

        id = data.get('id')
        recipient_id = data.get('recipient_id')

        user = CustomUser.objects.get(id=recipient_id)

        notification = Notification.objects.get(id=id)

        if (user != notification.recipient):
            return JsonResponse("error", safe=False)
            

        notification.state = 'Archive'
        notification.isAccept = True
        notification.save()

        smtp_server = SMTPServer()
        smtp_server.send_message(f'Здравствуйте - {user.fullName}, ОТВЕТ НА ЗАЯВКУ', GenerateMail(notification.sender, notification.project, True), user.email, html_content = None)

        return JsonResponse("ok", safe=False)
    
class RefusalApplication(View):
    def post(self, request):
        data = request.POST

        id = data.get('id')
        recipient_id = data.get('recipient_id')

        user = CustomUser.objects.get(id=recipient_id)

        notification = Notification.objects.get(id=id)

        if (user != notification.recipient):
            return JsonResponse("error", safe=False)
            

        notification.state = 'Archive'
        notification.isAccept = False
        notification.save()

        smtp_server = SMTPServer()
        smtp_server.send_message(f'Здравствуйте - {user.fullName}, ОТВЕТ НА ЗАЯВКУ', GenerateMail(notification.sender, notification.project, False), user.email, html_content = None)

        return JsonResponse("ok", safe=False)


def GenerateMail(user, project, success):
    message = ''
    if(success):
        if (project):
            message = f"<p>Пользователь {user.fullName} принял вашу заявку на участие в проекте {project.nameProject}</p>\n<p>Ожидайте, скоро он свяжется с вами!</p>"
        else:
            message = f"<p>Пользователь {user.fullName} принял вашу заявку с сотрудничеством</p>\n<p>Ожидайте, скоро он свяжется с вами!</p>"
    else:
        if (project):
            message = f"<p>Пользователь {user.fullName} отказал в вашей заявке на участие в проекте {project.nameProject}</p>"
        else:
            message = f"<p>Пользователь {user.fullName} не принял вашу заявку о сотрудничестве</p>"

    return message