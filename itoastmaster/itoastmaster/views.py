#coding=utf-8
from django.shortcuts import render

from login.models import UserInfo
from itoastmaster.common import get_email

def home(request):

    # description, icon, page, disable
    path = '/static/pic/'
    email = get_email(request)
    
    modules = [
        # ['Register', 'sign.jpg', 'register', True],
        # ['Login', 'enter.jpg', 'login', True],
        ['个人', 'home.jpg', 'profile', True],
        ['新闻', 'news.jpg', 'news', True],
        ['俱乐部', 'club.jpg', 'club', True],
        ['会员', 'people.jpg', 'member', True],
        ['鹊桥', 'love.jpg', 'lovebridge', True],
        ['CC手册', 'cc.jpg', 'cc_manual', False],
        ['CL手册', 'cl.jpg', 'cl_manual', False],
        ['投票最佳', 'vote.jpg', 'polls', False],
        ['智能计时器', 'timer.jpg', 'timer', False],
        ['视频', 'video.jpg', 'video', True],
        ['培训报名', 'sign.jpg', 'training', True],
        ['文档资料', 'material.jpg', 'material', True],
        
    ]
      
    for i in modules:
        i[1] = path + i[1]
        
    # row and colum    
    modules1 = []
    for i in range(len(modules)):
        if i % 3 == 0:
            modules1.append([])
        modules1[-1].append(modules[i])
        
    return render(request, 'common/home.html', {'modules' : modules1, 'email' : email})


def mine(request):
    
    name = 'Anybody'
    if 'email' in request.session:
        name = request.session['email']
    return render(request, 'common/mine_profile.html', {'name' : name})

def mine_words(request):

    return render(request, 'common/mine_words.html')

def mine_blog(request):
    
    return render(request, 'common/mine_blog.html')

def mine_photo(request):
    
    return render(request, 'common/mine_photo.html')

def mine_friends(request):
    
    return render(request, 'common/mine_friends.html')


def about(request):	
 
    return render(request, 'common/about.html', {'init' : "adfasdfasdfsad", 'email' : get_email(request)})
