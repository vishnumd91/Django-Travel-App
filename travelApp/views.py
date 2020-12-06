from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    name = {'name': 'vishnu'}
    return render(request, 'hello.html', name)
