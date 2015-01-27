from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *

# Create your views here.

def glowna(request):
	return render(request,'glowna.html',{})
def agents_list(request):
	agents = Agent.objects.filter().order_by('codename') # TODO: public and private
	return render(request,'agents_list.html',{'agents': agents})
def agentdetails(request,codename):
	agent = Agent.objects.get(codename=codename) # TODO: auth filtering
	return render(request,'agentdetails.html',{'agent': agent})
def login(request):
	return render(request,'login.html',{})
def login_error(request):
	return render(request,'login_error.html',{})
def newentry(request,codename):
	agent = Agent.objects.get(codename=codename) # TODO: auth filtering
	form = EntryForm(request.POST) if request.method == "POST" else EntryForm()
	if request.method == "POST" and form.is_valid():
		entry = form.save(commit=False)
		entry.added_time = timezone.now()
		entry.creator = request.user
		entry.agentdb = agent
		entry.save()
		return redirect('statsanalyze.views.agentdetails', codename=agent.codename)
	return render(request,'newentry.html',{'form': form, 'agent': agent})