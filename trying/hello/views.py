from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "hello/index.html")

def wait(request):
    return render(request, "hello/wait.html")

def wait2(request):
    return render(request, "hello/wait2.html")

def scroll(request):
    return render(request, "hello/scroll.html")

def repeate(request):
    return render(request, "hello/repeate.html")

def blend(request):
    return render(request, "hello/blend.html")

def move(request):
    return render(request, "hello/move.html")

def ending(request):
    return render(request, "hello/ending.html")