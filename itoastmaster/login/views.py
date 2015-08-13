from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import RequestContext
from django.core.context_processors import csrf

from login.models import User
from login.models import UserInfo
from login.form import RegisterInfo
from login.models import Province, City, Province1, School
from club.models import Club

from django.http import HttpResponseRedirect

from itoastmaster.common import get_email


def login(request):

    error = []
    
    if request.method == 'POST':
        
        if 'email' in request.POST and 'passwd' in request.POST:
            email = request.POST['email']
            passwd = request.POST['passwd']
            
            if not email:
                error.append('Email should not be NULL')
            if not passwd:
                error.append('Password should not be NULL')
            
            if email:
                user = User.objects.filter(email=email)
            
                if user:
                    user = User.objects.get(email=email, password=passwd)
                    if user:
                        request.session['email'] = email
                        request.session['name'] = email
                        userinfo = UserInfo.objects.get(email=email)
                        if userinfo.name:
                            request.session['name'] = userinfo.name
                        request.session['email'] = email
                        return HttpResponseRedirect('/home', {'email' : get_email(request)})
                    else:
                        error.append('Password is not correct')
                else:
                    error.append('%s does not exists!' % email)
       
    return render(request, 'login/login.html', {'title' : 'LOGIN', 'error' : error, 'csrf_token' : request.COOKIES['csrftoken']})


def logout(request):
    
    from itoastmaster.common import get_email
    email = get_email(request)
    
    if email:
        del request.session['email']
    
        userInfo = UserInfo.objects.filter(email=email)
        name = ''
        if userInfo:
            name = email
            return render(request, 'login/logout.html', {'name' : name})
    else:
        return HttpResponseRedirect('/home')


def is_valid(str):
    
    up_flag = False
    low_flag = False
    digit_flag = False
    oper_flag = False
    
    for i in str:
        if i.isdigit():
            digit_flag = True
        elif i.isalpha():
            if i.islower():
                low_flag = True
            elif i.isupper():
                up_flag = True
        else:
            oper_flag = True
            
    if up_flag and low_flag and digit_flag and oper_flag:
        return True
    else:
        return False
    
    
def register(request):
    
    error = []
    email = ''
    passwd = ''
    passwd1 = ''
    
    if request.method == 'POST':
        
        data = request.POST
        
        if 'email' in data and 'passwd' in data and 'passwd1' in data and (
            'icode' in data and 'icode_ref' in data):
            email = data['email']
            passwd = data['passwd']
            passwd1 = data['passwd1']
            error = []
            import re
            if not data['email']:
                error.append('Email should not be NULL')
            elif not re.match(u'\w+@\w+\.\w+', data['email']):
                    error.append(['Email is not correct'])
            
            user = User.objects.filter(email=email)
            if user:
                error.append('Email exists')
                
            if data['passwd'] != data['passwd1']:
                error.append('Twice Password are different')
            elif len(data['passwd']) < 8:
                error.append('Length of password should be 8 at least')
                error.append('Lower and upper character, digit and operator should have one at least')
            elif len(data['passwd']) > 100:
                error.append('Length of password should be less than 128')
            elif not is_valid(data['passwd']):
                error.append('Lower and upper alpha and digit and operator should have one at least')
                
            if not data['icode']:
                error.append('Identifying code should not be NULL')
            elif data['icode'].lower() != data['icode_ref'].split('.')[0].lower():
                error.append('Identifying code is not correct')
                
            if not error:
                email = data['email']
                password = data['passwd']
                user = User(email=email, password=password)
                user.save()
                
                userinfo = UserInfo(email=email, name=email, lovebridge=True)
                userinfo.save()
                
                # It's very important
                request.session['email'] = email
                request.session['name'] = email
                
                return render(request, 'login/register_succ.html', {'email' : user.email, 'passwd' : user.password, 'csrf_token' : request.COOKIES['csrftoken']})
    
    import os
    import random
    
    ident_pics = os.listdir('static/pic/verify')
    random.shuffle(ident_pics)
    
    return render(request, 'login/register.html', {'title' : 'LOGIN', 'ident_pic' : ident_pics[0], 'error' : error,
                                                   'email' : email, 'passwd' : passwd, 'passwd1' : passwd1})


def handle_uploaded_file(f, pic):
    
    destination = open('static/pic/upload/%s' % pic,'wb+')
    
    for chunk in f.chunks(): 
        destination.write(chunk)
    destination.close()
     
     
def register_info(request):

    # for generating select choice
    pro = Province.objects.order_by("name")
    city = City.objects.order_by("name")
    pro1 = Province1.objects.order_by("name")
    school = School.objects.order_by("name")
    club = Club.objects.order_by("name")
    
    error = []
    people = ''
    
    email = get_email(request)
        
    if email:
        try:
            people = UserInfo.objects.get(email=email)
        except:
            error.append('no UserInfo for %s' % email)

    if error:
        return render_to_response("login/register_info_fail.html", {'error' : error})   
               
    if not people:
        return HttpResponseRedirect('login')
         
    if request.method == 'POST':   
        data = request.POST
        
        people.name = request.POST['name']
        people.ename = request.POST['ename']    
        people.sex = data['sex']
        people.status = data['status']
        people.lovebridge = data['love']
        people.hometown = data['home1']
        people.school = data['school1']
        myclub = Club.objects.get(id=1)
        people.club = myclub
        people.join_dt = '-'.join([data['club_year'], data['club_month'], data['club_day']])
        people.speech = data['speech']
        people.leader = data['leader']
        people.positions = data['positions']
        people.interest = data['interest']
        people.self_introduction = data['self_intro']
        people.word = data['recent']
        people.phone = data['phone']
        people.born = '-'.join([data['born_year'], data['born_month'], data['born_day']])
        
        if 'pic' in request.FILES:
            pic_file = request.FILES['pic']
            if people.portrait_id:
                pic_name = '%s_%d.jpg' % (email, people.portrait_id)
                people.portrait_id += 1
            else:
                pic_name = email + '0.jpg'
                people.portrait_id = 1        
            handle_uploaded_file(pic_file, pic_name)
            people.portrait = pic_name
                
        people.save()
        
    return render_to_response("login/register_info.html", {'csrf_token' : request.COOKIES['csrftoken'],
                                                           'pro' : pro,
                                                           'city' : city,
                                                           'pro1' : pro1,
                                                           'school' : school,
                                                           'club' : club,
                                                           'people' : people,
                                                           'email' : email})
    
    
def profile(request):
    
    email = get_email(request)
    if not email:
        return HttpResponseRedirect('/login')
    
    people = UserInfo.objects.get(email=email)
    
    return render_to_response("login/profile.html", {'people' : people, 'email' : email})