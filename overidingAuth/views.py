from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from django.views.generic.edit import CreateView
from django.contrib.auth import *
from .forms import *
# Create your views here.

# def Parti_login(request):
#     form = Parti_Form(request.POST or None)
#     context = {
#         "form" : form,
#     }
#     return render(request, "overridingAuth/parti_index.html", context)

def Parti_login(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Create the form instance
        form = Parti_Form(request.POST)
        if form.is_valid():

            # refer to all the form fields
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # refer to the User model
            user = User(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                password = password
                )
            user.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = Parti_Form()

    return render(request, 'overridingAuth/parti_index.html', {'form': form})


# todo correct this thing up.
# class ContactView(FormView):
#     template_name = 'parti_index.html'
#     form_class = Parti_Form
#     success_url = '/thanks/'
#
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.send_email()
#         return super(ContactView, self).form_valid(form)
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
