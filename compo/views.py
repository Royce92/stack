from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
import json
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

def index (request):
    if request.method == "GET":
    return HttpResponse("hello test")
        

