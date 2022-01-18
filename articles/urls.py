from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path("", views.articleListView, name='list'),
    path("create/", views.createBlog, name="create"),
    path("<slug:slug>/", views.articleDetailView, name='detail'),
]