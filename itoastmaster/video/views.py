from django.shortcuts import render

# Create your views here.

import os

from itoastmaster.common import get_email
def video(request):
    
    import os
    videos = os.listdir('static/video')
    
    return render(request, 'video/video.html', {'videos' : videos, 'email' : get_email(request)})
