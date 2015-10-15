from django.shortcuts import render_to_response

# Create your views here.
from django.http import HttpResponse,Http404
import datetime

def index(request):
	return HttpResponse("Hello,this SkynetEye wolcome..!")

def test(request):

		h = "hello world!"

		return render_to_response("time.html",{"git_data":h})