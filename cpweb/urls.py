
from django.urls import path
from . import views

app_name = "cpweb"

urlpatterns = [
    path('clone-website/', views.clone_website, name='clone_website'),
]
