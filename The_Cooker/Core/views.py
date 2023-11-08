from django.shortcuts import render
from .models import CookingBlog
# Create your views here.


# Home page section
def Home(request):
    template = 'index.html'
    context = {
        'text' : 'Hello world!',
    }
    return render(request, template, context)




# Blogs section
def Blogs(request):
    blogs = CookingBlog.objects.all()
    template = 'blogs.html'
    context = {
        'blogs' : blogs,
    }
    return render(request, template, context)


def Blgo_about_page(request, pk):
    blog = CookingBlog.objects.get(id=pk)
    template = 'blog_about_page.html'
    context = {
        'blog' : blog,
    }
    return render(request,  template, context)
