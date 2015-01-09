from django.shortcuts import render
from .models import *

# Create your views here.

def agents_list(request):
	agents = Agent.objects.filter(public=True).order_by('codename')
	return render(request,'statsanalyze/agents_list.html',{'agents': agents})