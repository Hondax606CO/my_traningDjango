from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('about/', about, name='about'),
    path('coment/', coment, name='coment'),


]

