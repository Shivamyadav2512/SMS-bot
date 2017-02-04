from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import requests
import json

# Create your views here.

def test(request):
    return HttpResponse("testing succes")
