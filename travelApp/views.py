from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'index.html')


def add(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    res = num1 + num2
    return render(request, 'hello.html', {'result': res})
