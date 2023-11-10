from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.defaults import page_not_found
from .views import *
urlpatterns = [
    # home section
    path('', Home, name='home'),

    # searchbar section
    path('search/', Searchbar, name='searchbar'),

    # Blog section
    path('blogs/', Blogs, name='blogs'),
    path('blog/<int:pk>/', Blgo_about_page, name='blog_about_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = custom_404
