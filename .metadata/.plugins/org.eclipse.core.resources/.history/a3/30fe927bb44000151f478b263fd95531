from django.forms import ModelForm
from django import forms

from login.models import UserInfo

sex_choice = ( 
     ('', u"---------"), 
     (1, u"Male"),         
     (2, u"Female")
 )

status_choice = ( 
     ('', u"---------"), 
     (1, u"Single"),         
     (2, u"Married"),
     (3, u'Loving'),
     (4, u'Available'),
     (5, u'Not Available'),
 ) 

class RegisterInfo(ModelForm):
    
    sex = forms.ChoiceField(required=False, choices=sex_choice)
    status = forms.ChoiceField(required=False, choices=status_choice)
    join_dt = forms.DateInput()
    
    class Meta: 
         model = UserInfo
         fields = ('name', 'sex', 'status', 'lovebridge', 'hometown', 'school', 
                   'club', 'join_dt', 'progress', 'positions',
                   'interest', 'self_introduction', 'word')
    
    