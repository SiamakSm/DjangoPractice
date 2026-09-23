from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("hello django")


def say_my_name(request, name):
    return HttpResponse(f"Your name is {name}")


def guess_my_age(request, age):
    return HttpResponse(f"Your have {age} years old")


def guess_my_info(request, name, age):
    return HttpResponse(f"Your name is {name} and you have {age} years old")