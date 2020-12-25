from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def trialview(request):
	return HttpResponse("Hello there!")