from django.conf.urls import url
from eventApp import views

urlpatterns = [
    url(r'^EventList/$', views.event_list),
    #url(r'^EventList/(?P<pk>[0-9]+)/$', views.event_detail),
]
