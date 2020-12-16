from django.shortcuts import render

from .models import Link
from .forms import LinkForm, RawLinkForm

# Create your views here.
def link_home_view(request):
	queryset = Link.objects.all() # list of objects
	context = {
		"link_list": queryset
	}
	return render(request, "link_home.html", context)


def link_list_view(request):
	queryset = Link.objects.all() # list of objects
	context = {
		"link_list": queryset
	}
	return render(request, "link_list.html", context)



def link_create_view(request):
	form = LinkForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = LinkForm() 

	context = {
		'form': form
	}
	return render(request, "link_create.html", context)