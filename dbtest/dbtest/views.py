from django.shortcuts import render
from .models import MyBoard

def index(request):
    myboard = MyBoard.objects.all()
    return render(request, 'index.html', {'list': myboard})