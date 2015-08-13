from django.shortcuts import render

# Create your views here.

from club.models import Club
from itoastmaster.common import get_email

def club(request, page):
    
    try:
        page = int(page)
    except:
        page = 1
        
    sort_by_id = 0
    
    id_name = ['name', 'city_id', 'week']
               
    if request.method == 'GET':
        if 'page' in request.method:
            page = int(request.method['page'])
    
    clubs = Club.objects.order_by('name')
    
    total = len(clubs)
    num = 10
    pages = total/num
    left = num * page
    right = left + num
    if right > total:
        right = total
    
    return render(request, 'club/club.html', {'clubs' : clubs[left:right], 'pages' : range(1,pages),
                                              'email' : get_email(request)})
