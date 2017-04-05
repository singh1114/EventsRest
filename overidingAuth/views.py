from django.shortcuts import render
from .models import *
from django.views.generic.edit import CreateView
from django.contrib.auth import *
from .forms import *
# Create your views here.

def Parti_login(request):
    form = Parti_Form(request.POST or None)
    context = {
        "form" : form,
    }
    return render(request, "overridingAuth/parti_index.html", context)


# class Parti_index(CreateView):
#
#
#
#     model = User
#     fields = ['first_name', 'last_name', 'username', 'email', 'password']
#
#     template_name = 'overridingAuth/parti_index.html'
#
# class Parti_login(CreateView):
#     form = Parti_Form
#
#     template_name = 'overridingAuth/parti_index.html'
