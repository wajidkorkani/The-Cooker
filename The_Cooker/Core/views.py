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


# Searchbar section
def Searchbar(request):
    if request.method == "POST":
        searched = request.POST.get('search')
        blogs_title = CookingBlog.objects.filter(title__icontains=searched)
        blogs_name = CookingBlog.objects.filter(recipe_name__icontains=searched)
        blogs_exit_title = CookingBlog.objects.filter(title__iexact=searched)
        blogs_exit_name = CookingBlog.objects.filter(recipe_name__iexact=searched)
        template = 'searchbar.html'
        context = {
            'blogs_name' : blogs_name,
            'blogs_title' : blogs_title,
            'blog_exict_title': blogs_exit_title,
            'blog_exict_name' : blogs_exit_name,
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
