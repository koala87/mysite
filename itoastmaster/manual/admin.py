from django.contrib import admin

# Register your models here.
from manual.models import Manual, Objective

admin.site.register(Manual)

admin.site.register(Objective)
