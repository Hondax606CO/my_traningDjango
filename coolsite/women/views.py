from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import AddPostForm


menu = [{'title': 'Блог', 'url_name': 'about'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Вход', 'url_name': 'login'},
]


def index(request):
    last_post = Women.objects.all()[:1]
    contact_list = Women.objects.all()[1:]

    paginator = Paginator(contact_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'last_post': last_post,
               'page_obj': page_obj,
               'menu': menu,
               }
    return render(request, 'women/index.html', context=context, )


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    posts = Women.objects.all()
    context = {'post': post,
               'posts': posts,
                'menu': menu,
               'title': 'Главная страница',
               'cat_selected': 0,
               }
    return render(request, 'women/show_post.html', context=context)


def about(request):
    return render(request, 'women/about.html')


def coment(request):
    coment = Coment.objects.all()
    form = AddPostForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'women/coment.html', {'form': form, 'coment': coment})







