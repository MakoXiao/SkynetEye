from django.shortcuts import render_to_response

# Create your views here.
from django.http import HttpResponse,Http404
import datetime

def index(request):

		return render_to_response("index.html")

def test(request):
	return HttpResponse("Hello,this SkynetEye wolcome..!")
