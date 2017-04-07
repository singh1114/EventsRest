from django.conf.urls import url
from overidingAuth import views
from .views import *
from .forms import *

urlpatterns = [
    url(r'^parti_signup/', views.Parti_signup, name = 'parti_signup'),
    url(r'^parti_login', views.Parti_login, name = 'parti_login')
]
