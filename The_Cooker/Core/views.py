from django.shortcuts import render
from .models import CookingBlog
# Create your views here.

# Home page section
def Home(request):
        def boot():
            text = blogs_title = blogs_name = blogs_exit_name = blogs_exit_title = ''
            if request.method == "POST":
                input_text = request.POST.get('text')
                if input_text in ['what is your name', 'who are you?', 'who are you', 'your name', 'what is your name?', 'your name?', 'name?', 'name']:
                    text = 'My name is The Cooker'
                elif input_text in ['what you can do', 'what you can do?', 'what can you do', 'what can you do?', 'give me your introduction', 'introduce your self', 'what are you?']:
                    text = "Hello, My name is The Cooker and I am an artificial intelligance 'Al' and I can help you with cooking."
                elif CookingBlog.objects.filter(title__icontains=input_text):
                    blogs_title = CookingBlog.objects.filter(title__icontains=input_text)
                elif CookingBlog.objects.filter(recipe_name__icontains=input_text):
                    blogs_name = CookingBlog.objects.filter(recipe_name__icontains=input_text)
                elif CookingBlog.objects.filter(title__iexact=input_text):
                    blogs_exit_title = CookingBlog.objects.filter(title__iexact=input_text)
                elif CookingBlog.objects.filter(recipe_name__iexact=input_text):
                    blogs_exit_name = CookingBlog.objects.filter(recipe_name__iexact=input_text)
                else:
                    text = 'Hello'
                return text, blogs_title, blogs_name, blogs_exit_name, blogs_exit_title
            else:
                input_text = 'Hello'
                text = input_text
                blogs_title = input_text
                blogs_name = input_text
                blogs_exit_name = input_text
                blogs_exit_title = input_text
            return text, blogs_title, blogs_name, blogs_exit_name, blogs_exit_title
        text, blogs_title, blogs_name, blogs_exit_name, blogs_exit_title = boot()
        template = 'index.html'
        context = {
            'text' : text,
            'blogs_name' : blogs_name,
            'blogs_title' : blogs_title,
            'blog_exict_title': blogs_exit_title,
            'blog_exict_name' : blogs_exit_name,
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
            'blogs_exict_name' : blogs_exit_name,
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
