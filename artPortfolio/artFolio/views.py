from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse




def index(request):
	return render(request, "artFolio/index.html")

def simple_view(request):
	return HttpResponse("Simple View")


def detail(request, artwork_id):
	return HttpResponse("You're looking at artwork %s" % artwork_id)


def example_view(request):
	return render(request, "artFolio/example.html")
