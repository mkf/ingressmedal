from django.shortcuts import render
from .models import *

# Create your views here.

def agents_list(request):
	agents = Agent.objects.filter(public=True).order_by('codename')
	return render(request,'agents_list.html',{'agents': agents})
def login(request):
	return render(request,'login.html',{})