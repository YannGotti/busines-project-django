from user.models import Notification

def current_path(request):
    return {
        'current_path': request.path
    }

def common_notifications(request):
    user = None
    notifications = None
    try:
        user = request.user
    except:
        notifications = None
    try:
        notifications = Notification.objects.filter(recipient=user, state='Active')
    except:
        notifications = None
    
    context = {
        'notifications': notifications,
    }

    return context