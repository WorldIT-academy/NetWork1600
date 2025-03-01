from django.shortcuts import render,redirect
from .models import Post, Tag
from django.contrib.auth.decorators import login_required
from user.models import Profile
from .forms import PostForm, TagForm
from django.contrib.admin.views.decorators import staff_member_required


def render_all_posts(request):
    all_posts = Post.objects.all()
    return render(request=request, template_name='post/all_posts.html', context = {"all_posts": all_posts})

# Декоратор перевіряє, якщо користувач не авторизувався - його треба перекинути на сторінку авторизації
@login_required
def render_create_posts(request):
    # Якщо тип запиту POST (якщо користувач наділса форму)
    if request.method == 'POST':
        # Свторюємо об'єкт форми та "наповнюємо" її даними та файлами, які користувач надіслав через форму
        form = PostForm(request.POST, request.FILES)
        # Перевірка даних на валідінсть, тобто якщо дані введені коректно та віповідають усім вимогам, що описані у класі PostForm
        if form.is_valid():
            # Отримуємо проіфль автора на основі поточного користувача
            author = Profile.objects.get(user = request.user)
            # Зберагіємо форму (та передаємо автора поста)
            form.save(author_profile = author)
            return redirect('all_posts')
    else: 
        # Створюємо об'єкт порожньої форми, щоб її відобразити на сторінці
        form = PostForm()
        
    return render(request=request, template_name='post/create_post.html', context = { "form": form})

@staff_member_required
def render_create_tag(request):
    # Якщо тип запиту POST (якщо користувач наділса форму)
    if request.method == 'POST':
        # Свторюємо об'єкт форми та "наповнюємо" її даними та файлами, які користувач надіслав через форму
        form = TagForm(request.POST, request.FILES)
        # Перевірка даних на валідінсть, тобто якщо дані введені коректно та віповідають усім вимогам, що описані у класі PostForm
        if form.is_valid():
            # Зберагіємо форму (та передаємо автора поста)
            form.save()
            return redirect('all_tags')
    else: 
        # Створюємо об'єкт порожньої форми, щоб її відобразити на сторінці
        form = TagForm()
        
    return render(request=request, template_name='post/create_tag.html', context = { "form": form})


def render_all_tags(request):
    tags = Tag.objects.filter(is_active = True)
    return render(request=request, template_name="post/all_tags.html", context= {"tags": tags})