from django.shortcuts import render

from login.models import UserInfo

def home(request):

    # description, icon, page, disable
    path = '/static/pic/'
    modules = [
        #['Register', 'sign.jpg', 'register', True],
        #['Login', 'enter.jpg', 'login', True],
        ['Profile', 'home.jpg', 'register_info', True],
        ['News', 'news.jpg', 'news', True],
        ['Clubs', 'club.jpg', 'club', True],
        ['Members', 'people.jpg', 'member', True],
        ['Lovebridge', 'love.jpg', 'lovebridge', True],
        ['CC Manual', 'cc.jpg', 'cc_manual', False],
        ['CL Manual', 'cl.jpg', 'cl_manual', False],
        ['Vote Best', 'vote.jpg', 'polls', False],
        ['Brain Timer', 'timer.jpg', 'timer', False],      
        ['Video', 'video.jpg', 'video', True],
        ['Training', 'sign.jpg', 'training', True],
        ['Material', 'material.jpg', 'material', True],
        
    ]
    
    if False:
        email = ''
        if 'email' in request.session:
            email = request.session['email']
        
        if email:
            people = UserInfo.objects.filter(email=email)
            if people:
                modules[0] = ['Profile', 'home.jpg', 'register_info', True]
                del modules[1]
                modules.append(['Logout', 'exit.png', 'logout'])
    
    for i in modules:
        i[1] = path + i[1]
        
        
    modules1 = []
    for i in range(len(modules)):
        if i % 3 == 0:
            modules1.append([])
        modules1[-1].append(modules[i])
        
    return render(request, 'common/home.html', {'modules' : modules1})


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
    
    return render(request, 'common/about.html')
