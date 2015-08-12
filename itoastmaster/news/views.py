from django.shortcuts import render

# Create your views here.

from news.models import News

def news(request):
    
    if request.method == 'GET':
        if 'nid' in request.GET:
            nid = request.GET['nid']
            
            nid = int(nid)
            news = News.objects.all()[nid-1];
            
            if news:
                return render(request, 'news/news_view.html', {'news' : news, 'nid' : nid})          
            
    news = News.objects.all()
        
    return render(request, 'news/news.html', {'news' : news})


def news_new(request):
        
    if request.method == 'GET':
        if 'name' in request.GET and 'content' in request.GET and 'title' in request.GET:
            name = request.GET['name']
            title = request.GET['title']
            content = request.GET['content']
            date = '1987-02-02'
            time = '10:0:0'
                
            news = News(name=name, title=title, content=content, dt=date, time=time)
            news.save()
        
            return render(request, 'news/news_succ.html', {'title' : title, 'content' : content})

    return render(request, 'news/news_new.html')


def news_view(request):

    news = News.objects.all()
        
    if request.method == 'GET':
        if 'name' in request.GET and 'content' in request.GET and 'nid' in request.GET:
            name = request.GET['name']
            content = request.GET['content']
            nid = request.GET['nid']
            
            news = News.objects.all()[nid-1];
            
            if news:
                return render(request, 'news/news_view.html', {'news' : news, 'nid' : nid})    
        
    return render(request, 'news/news.html')