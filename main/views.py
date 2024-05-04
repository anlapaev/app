from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
    }
    return render(request, "main/index.html", context=context)


def about(request):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Магазин классный и товар хороший",
    }
    return render(request, "main/about.html", context=context)
