from django.shortcuts import render

# Create your views here.

def material(request):
    
    return render(request, 'material/material.html')