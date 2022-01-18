from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path("signup/", views.signUpView, name='signup'),
    path("login/", views.logInView, name="login"),
    path("logout/", views.logOutView, name="logout"),
]