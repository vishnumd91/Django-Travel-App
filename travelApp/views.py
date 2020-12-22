from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, News
# from datetime import date


def home(request):
    placeDetails = Place.objects.all()
    newsPosts = News.objects.all()
    # dateDetails = date()
    # newsDateFilter = News.objects.filter(
    #     day__day__gte=dateDetails.day,
    #     day__month__gte=dateDetails.month
    # )
    return render(request, 'index.html', {'data': placeDetails, 'newsData': newsPosts})

# def news(request):
#     newsPosts = News.objects.all()
#     return render(request, 'index.html', {'newsData': newsPosts})

# def add(request):
#     num1 = int(request.POST['num1'])
#     num2 = int(request.POST['num2'])
#     res = num1 + num2
#     return render(request, 'hello.html', {'result': res})
