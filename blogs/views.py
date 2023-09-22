from django.shortcuts import render
from .models import blog
from django.shortcuts import get_object_or_404, render



from . import views

def index(request):
    return render(request, 'index.html')

def allblogs(request):
    bg = blog.objects.all()
    return render(request, "blog/blogs.html", {'bg':bg})

def blog_detail(request, slug):
    bg_all = blog.objects.all()
    bg_single = get_object_or_404(blog, slug=slug)
    return render(request, "single/blogdetails.html", {'bg_single': bg_single, "bg_all": bg_all })

def extension(request):
    return render(request, "extension.html")

def searchfunc(request):        
    if request.method == 'GET':      
        query =  request.GET.get('query')      
        if query:
            products = blog.objects.filter(title__contains=query)
        return render(request,"searchbaar.html",{"products":products})
    else:
        print("No informations found")
        return render(request, "searchbaar.html", {})
    
    
    
