from django.shortcuts import render

# Create your views here.

from login.models import UserInfo
from itoastmaster.common import get_email

def member(request):

    people = UserInfo.objects.all()
        
    return render(request, 'member/member.html', {'people' : people, 'email' : get_email(request)})
