from django.shortcuts import render,redirect
from .models import Post, Tag
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
import os
from user.models import Profile
from .forms import PostForm


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