from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime as dt
from playground import urls
from .models import *

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    title='Playground'
    profiles= Profile.objects.all()
    current_user = request.user
    return render(request, 'welcome.html',{title:'title',"profiles":profiles,"current_user":current_user})

@login_required(login_url='/accounts/login/')
def profile(request,id):
    user_object = request.user
    current_user = Profile.objects.get(username__id=request.user.id)
    user = Profile.objects.get(username__id=id)

    return render(request, "profile.html", {"current_user":current_user,"user":user,"user_object":user_object})