from django.contrib import admin

# Register your models here.

from login.models import User, UserInfo, Province, City, Province1, School

admin.site.register(User)

admin.site.register(UserInfo)

admin.site.register(Province)

admin.site.register(City)

admin.site.register(Province1)

admin.site.register(School)
