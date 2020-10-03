from django.http import HttpResponse
from django.shortcuts import render

def ind(request):
    return render(request,'Blog\index.html')

