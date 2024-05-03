from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        "title": "Home",
        "content": "Главная страница",
    }
    return render(request, "main/index.html", context=context)


def about(request):
    return HttpResponse("about page")
