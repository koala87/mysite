#coding=utf-8
'''
Created on 2015年8月13日

@author: jyqi
'''

def is_login(request):
    if 'email' in request.session and request.session['email']:
        return True
    else:
        return False
    
def get_email(request):
    
    if is_login(request):
        return request.session['email']
    else:
        return ''
    
def name(request):
    if 'name' in request and request['name']:
        return request['name']
    else:
        return ''