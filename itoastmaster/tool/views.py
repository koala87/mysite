from django.shortcuts import render

# Create your views here.

from itoastmaster.common import get_email

def timer(request):
    
    return render(request, 'tool/timer.html', {'email' : get_email(request)})