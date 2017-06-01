from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import *
from eventApp.models import EventList

from django.views.generic.edit import CreateView
from django.contrib.auth.models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin

# This library is used to encrypt the password given by the user
from django.contrib.auth.hashers import make_password
# Create your views here.

# This is the sign up view of participant
def Parti_signup(request):
    if request.user.is_authenticated():
         return HttpResponseRedirect("/parti_tasks/")
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
            user.groups.add(1)
            user.save()

            # If the form is filled perfectly
            return HttpResponseRedirect('/parti_login/')
    else:
        form = Parti_signup_form()
    # If the user lands up to the page for the first time.
    # And if the form is not perfectly filled.
    return render(request, 'overridingAuth/parti_signup.html', {'form': form})

# This view is for the login of participant.
def Parti_login(request):
    
	if request.user.is_authenticated():
         return HttpResponseRedirect("/parti_tasks/")
    
	# Initialize a variable to check if a URL has a next parameter
	next = ""

	# If it is GET request
	if request.GET:
		next = request.GET['next']

	# If the request method is post i.e. if the form is posted.
	if request.method == 'POST':
		form = Parti_login_form(request.POST)
		if form.is_valid():
			Username = form.cleaned_data.get('username')
			Password = form.cleaned_data.get('password')

            # Find the username in the User model.
			user = User.objects.get(
                username = Username
            )

            # if the user is Not None
			if user is not None:
                # If the group of the particular user is participant.

				group = user.groups.get(user = user)
				if group.name == 'participant':
					user = authenticate(
		        		username = Username, 
		        		password = Password
		    	)
				# The backend authenticated the user
				if user is not None:
					if user.is_active:
						login(request, user)
                        # Go to this URL if the login is successful

						# check if the next is empty or not
						if next == "":
							return HttpResponseRedirect('/parti_tasks/')

						else:
							return HttpResponseRedirect(next)

				# The backend didn't authenticated the user
				else:
					return HttpResponseRedirect('/parti_login/')
    # If the form is not posted.
	else:
		form = Parti_login_form()

	return render(request, 'overridingAuth/parti_login.html', {'form': form})

# Let's write the class based view for the basic home page
class Home_parti_tasks(TemplateView):
    template_name = 'overridingAuth/login_success.html'

# The view to that allow the addition of profile by the participant
class addProfile(LoginRequiredMixin, CreateView):  
    # login fail credentials
	login_url = '/parti_login'
    
    # if the user is already logged in 
	model = Participant
	fields = [
	'Participant_F_Name',
	'Participant_L_Name',
	'Participant_Branch',
	'Participant_Year',
	'Participant_roll_number',
	'Participant_phone_number',
	'Participant_email'
	]
	template_name = 'overridingAuth/add_profile.html'
    
    # When form is received with valid data go to this url
	success_url = '/parti_tasks/'
	
    # Define this function to pre-populate the fields with some values
	def get_initial(self):
		initials = {
			'Participant_F_Name': self.request.user.first_name,
			'Participant_L_Name': self.request.user.last_name,
			'Participant_email': self.request.user.email
		}		
		return initials 
    # Alternatively we can use this implementation
    # initial = {'Participant_F_Name': 'Mr. Khan Sama'}


    # This function works whenever valid data is pushed 
    # Default implementation does this
    # simply redirects to success_url
    # For the CreateView this function fill db by itself
	def form_valid():
    	# For the time being let's not add anything up here
		pass

# View to show all the events present in the database

class eventList(ListView):
	model = EventList
	template_name = 'overridingAuth/eventlist.html'
