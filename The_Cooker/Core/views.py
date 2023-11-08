from django.shortcuts import render
from .models import CookingBlog
# Create your views here.
def Home(request):
    template = 'index.html'
    context = {
        'text' : 'Hello world!',
    }
    return render(request, template, context)

def Blogs(request):
    blogs = CookingBlog.objects.all()
    template = 'blogs.html'
    context = {
        'blogs' : blogs,
    }
    return render(request, template, context)
