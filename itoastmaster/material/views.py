from django.shortcuts import render

# Create your views here.

from itoastmaster.common import get_email

def material(request):
    
    return render(request, 'material/material.html', {'email' : get_email(request)})