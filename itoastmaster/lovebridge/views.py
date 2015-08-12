from django.shortcuts import render

# Create your views here.

from login.models import UserInfo

def lovebridge(request):
    
    people = UserInfo.objects.all()
    
    return render(request, 'lovebridge/lovebridge.html', {'people' : people})