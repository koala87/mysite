from django.shortcuts import render

# Create your views here.

from login.models import UserInfo

def member(request):

    people = UserInfo.objects.all()
        
    return render(request, 'member/member.html', {'people' : people})
