import datetime
import os
from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Обновить': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях 
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().time()
    msg = f"""   
    <form action="/"">
        <button>Назад</button>
    </form><br>Текущее время: <b>{current_time}</b>"""
    return HttpResponse(msg)


def workdir_view(request):
    listdir = os.listdir()
    strdir = "<li>" + "<li>".join(listdir)
    back = """
            <form action="/" >
                <button>Назад</button>
            </form><br>"""
    return HttpResponse(back + strdir)
