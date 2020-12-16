from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args, **kwargs):
	context = {"Authors": ["William Part", "Sunpyo Hong"]}
	return render(request, "home.html", context)
	# return HttpResponse("<h>Hello World</h>")