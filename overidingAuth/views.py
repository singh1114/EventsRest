from django.shortcuts import render
from .models import *
from django.views.generic.edit import CreateView
from django.contrib.auth import *
# Create your views here.

class Parti_index(CreateView):



    model = User
    fields = ['first_name', 'last_name', 'username', 'email', 'password']

    template_name = 'overridingAuth/parti_index.html'
