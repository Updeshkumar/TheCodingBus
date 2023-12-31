
from django.urls import path
from . import views


app_name = "blogs"

urlpatterns = [
    path('', views.index, name="index"),
    
    path('blog/', views.allblogs, name="blog"),
    path('<slug:slug>', views.blog_detail, name="blog_detail"),
    path('search/', views.searchfunc, name="search"),
    path('extension/', views.extension, name="extension")
   
]
