from django.contrib import admin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
import datetime



def books_list_view(request):
    if request.method == 'GET':
        books_list = models.Books.objects.filter().order_by('-id')
        context = {'books_list': books_list}
        return render(request, template_name='book.html', context=context)

def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Books, id=id)
        context = {'book_id': book_id}
        return render(request, template_name='book_detail.html', context=context)




def about_me(request):
    if request.method == 'GET':
        return HttpResponse("Hi! My name is Asema and I study in GEEKS. I'm 16 y.o.")


def about_my_pet(request):
    if request.method == 'GET':
        return HttpResponse("<img src='https://s0.rbk.ru/v6_top_pics/media/img/9/73/756723943137739.webp'>- This is my cat, Barni", )


def system_time(request):
    if request.method == 'GET':
        return HttpResponse(datetime.datetime.now())

