from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from django.views.generic.edit import CreateView
from django.contrib.auth import *
from .forms import *

# This library is used to encrypt the password given by the user
from django.contrib.auth.hashers import make_password
# Create your views here.

# This is the sign up view
def Parti_signup(request):
    # Check if the request method is POST
    if request.method == 'POST':

        # Create the form instance
        form = Parti_signup_form(request.POST)
        if form.is_valid():

            # refer to all the form fields
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # Encrypt the password
            password = make_password(password)
            # refer to the User model

            user = User(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                password = password,
                is_staff = True,
                )

            # Now save the user in the database
            user.save()

            # It is very important to use this code here.
            # Once the user is added we can change the group to the user.
            user.groups.add(2)
            user.save()

            # If the form is filled perfectly
            return HttpResponseRedirect('/thanks/')
    else:
        form = Parti_signup_form()
    # If the user lands up to the page for the first time.
    # And if the form is not perfectly filled.
    return render(request, 'overridingAuth/parti_index.html', {'form': form})

#
