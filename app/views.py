from django.shortcuts import render
from django.http import HttpResponse
import os

def one(request):
    return HttpResponse("Hello")


def sam(request):
    return render(request,"sample.html")


