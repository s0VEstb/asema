from django.shortcuts import render
from django.http import HttpResponse
import datetime


def about_me(request):
    if request.method == 'GET':
        return HttpResponse("Hi! My name is Asema and I study in GEEKS. I'm 16 y.o.")


def about_my_pet(request):
    if request.method == 'GET':
        return HttpResponse("<img src='https://s0.rbk.ru/v6_top_pics/media/img/9/73/756723943137739.webp'>- This is my cat, Barni", )


def system_time(request):
    if request.method == 'GET':
        return HttpResponse(datetime.datetime.now())

