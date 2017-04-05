from django.conf.urls import url
from overidingAuth import views
from .views import *
from .forms import *

urlpatterns = [
    #url(r'^overidingAuth/$', views.overidingAuth),
    # import the classbased views for the participant index page
    url(r'^parti_index/', views.Parti_login, name = "participation_index"),
    #url(r'^parti_login', views.Parti_login.as_view(), {'authentication_form': Parti_Form})
]
