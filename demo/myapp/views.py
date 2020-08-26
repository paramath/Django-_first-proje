from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now
    print(now)
    return HttpResponse ("This is my website")

# Create your views here.
