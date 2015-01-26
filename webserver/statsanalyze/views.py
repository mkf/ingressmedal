from django.shortcuts import render
from .models import *

# Create your views here.

def glowna(request):
	return render(request,'glowna.html',{})
def agents_list(request):
	agents = Agent.objects.filter(public=True).order_by('codename')
	return render(request,'agents_list.html',{'agents': agents})
def login(request):
	return render(request,'login.html',{})
def login_error(request):
	return render(request,'login_error.html',{})