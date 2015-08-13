from django.shortcuts import render

# Create your views here.

from manual.models import Manual, Objective

from itoastmaster.common import get_email

def cc_manual(request):
    
    manual = Manual.objects.filter(kind="cc")

    return render(request, 'manual/manual.html', {'manual' : manual, 'kind' : 'cc', 'email' : get_email(request)})


def cl_manual(request):
    
    manual = Manual.objects.filter(kind='cl')
    
    return render(request, 'manual/manual.html', {'manual' : manual, 'kind' : 'cl', 'email' : get_email(request)})