from django.conf.urls import url
from overidingAuth import views
from .views import *
from .forms import *

urlpatterns = [
    url(r'^parti_signup/', views.Parti_signup, name = 'parti_signup'),
    url(r'^parti_login', views.Parti_login, name = 'parti_login'),
    url(r'^parti_tasks/', views.Home_parti_tasks.as_view(), name = 'parti_tasks'),

    # URL to add profile for a participant
    url(r'^add_profile', views.addProfile.as_view(), name = 'add_profile'),
	
	# URL to list all the events in database
	url(r'^all_events', views.eventList.as_view(), name = 'all_events')
]
