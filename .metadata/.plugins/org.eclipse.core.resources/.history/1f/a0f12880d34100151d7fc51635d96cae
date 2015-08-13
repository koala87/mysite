from django.shortcuts import render

# Create your views here.

def video(request):
    
    import os
    videos = os.listdir('static/video')
    
    return render(request, 'video/video.html', {'videos' : videos})
