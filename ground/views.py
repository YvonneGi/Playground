from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from playground import urls
from .models import *

# Create your views here.
def welcome(request):
    title='Playground'
    return render(request, 'welcome.html',{title:'title'})