from django.http import HttpResponse
from django.shortcuts import render

def homeView(request):
    # return HttpResponse('Home')
    return render(request, 'index.html')


def aboutView(request):
    # return HttpResponse('About')
    return render(request, 'about.html')
