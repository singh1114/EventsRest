from django.conf.urls import url
from overidingAuth import views

urlpatterns = [
    #url(r'^overidingAuth/$', views.overidingAuth),
    # import the classbased views for the participant index page
    url(r'^parti_index/', views.Parti_index.as_view(), name = "participation_index")
]
