#coding=utf-8

from django.forms import ModelForm
from django import forms

from login.models import UserInfo

sex_choice = ( 
     ('', u"---------"), 
     (1, u"男"),         
     (2, u"女")
 )

status_choice = ( 
     ('', u"---------"), 
     (1, u"未婚"),         
     (2, u"已婚"),
     (3, u'恋爱中'),
     (4, u'忙碌中'),
 ) 

class RegisterInfo(forms.Form):
    
    name = forms.CharField(label="姓名")
    sex = forms.ChoiceField(required=False, choices=sex_choice, label="性别")
    born = forms.CharField(label="出生日期")
    status = forms.ChoiceField(required=False, choices=status_choice, label="状态")
    lovebridge = forms.BooleanField(label="参加鹊桥")
    hometown = forms.CharField(label="家乡")
    school = forms.CharField(label="学校")
    club = forms.CharField(label="参加俱乐部")
    join_dt = forms.CharField(label="加入时间")
    progress = forms.CharField(label="演讲进度")
    positions = forms.CharField(label="担任职务")
    interest = forms.CharField(label="兴趣")
    self_introduction = forms.CharField(label="自我介绍")
    word = forms.CharField(label="发表说说")
         
         
    
    