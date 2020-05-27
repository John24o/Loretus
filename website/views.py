from datetime import time, datetime, timezone, timedelta
from django.urls import reverse, resolve
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse, Http404
from django.db import transaction

# Create your views here.
def home(request):
    print("HOLA")
    return render(
        request,
        'loreto/index.html',
        context={},
    )
