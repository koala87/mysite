#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

from news.models import News

from itoastmaster.common import get_email

def news(request):
    
    news = News.objects.filter(display=1).order_by('raw_time')
    news = news.reverse()
    email = get_email(request)

    return render(request, 'news/news.html', {'news' : news,
                                              'csrf_token' : request.COOKIES['csrftoken'],
                                              'email' : email})


def news_new(request):
        
    email = get_email(request)
    if request.method == "POST":
        name = request.session['name']
        import time
        tmp = time.localtime()
        raw_time = time.time()
        dt = '-'.join(['%d' % i for i in tmp[:3]])
        time = ':'.join(['%d' % i for i in tmp[3:6]])
        title = request.POST['title']
        content = request.POST['content']
        news = News(name=name, title=title, content=content, dt=dt, time=time, raw_time=raw_time, email=email, display=True)
        news.save()
        
        return HttpResponseRedirect('news')

    return render(request, 'news/news_new.html', {'csrf_token' : request.COOKIES['csrftoken'],
                                                  'email' : email})


def news_view(request, pid):
  
    try:
        id = int(pid)
    except:
        id = 1
        
    news = News.objects.get(id=id)
    
    return render(request, 'news/news_view.html', {'news' : news, 'csrf_token' : request.COOKIES['csrftoken'],
                                                   'email' : get_email(request)})



def news_del(request, pid):
  
    try:
        id = int(pid)
    except:
        id = 1
        
    news = News.objects.get(id=id)
    
    news.display = 0
    
    news.save()
    
    return HttpResponseRedirect('/news')


def news_modify(request, id):
        
    news = News.objects.get(id=id)
    
    title = news.title
    content = news.content
    
    if request.method == "POST":
        news.title = request.POST['title']
        news.content = request.POST['content']
        
        news.save()
        
        return HttpResponseRedirect('/news')

    return render(request, 'news/news_modify.html', {'csrf_token' : request.COOKIES['csrftoken'],
                                                  'title' : title,
                                                  'content' : content})