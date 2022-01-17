from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path("", views.articleListView, name='list'),
    path("<slug:slug>/", views.articleDetailView, name='detail'),
]