from django.shortcuts import render

# Create your views here.

def agents_list(request):
	return render(request,'statsanalyze/agents_list.html',{})