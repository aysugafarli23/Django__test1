from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello world!')
    
def products_news(reques):
    return HttpResponse('I am news page of products page ')

def product1(reuqest):
    return HttpResponse("I'm Product1 -Milk")

def product2(request):
    return HttpResponse("I'm Product2 - Coffee")

def product3(request):
    return HttpResponse("I'm product3 - Chocolate")

