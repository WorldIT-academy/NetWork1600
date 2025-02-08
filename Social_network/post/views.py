from django.shortcuts import render,redirect
from .models import Post, Tag
from django.core.files.storage import FileSystemStorage
import os
from user.models import Profile


def render_all_posts(request):
    all_posts = Post.objects.all()
    return render(request=request, template_name='post/all_posts.html', context = {"all_posts": all_posts})

def render_create_posts(request):
    # Отримуємо усі теги, щоб потім їх відобразити у формі
    all_tags = Tag.objects.all()
    # Якщо тип запиту POST (якщо користувач наділса форму)
    if request.method == 'POST':
        # Отримуємо заголовок для публікації з форми
        title = request.POST.get('title')
        # Отримує контент для публікації з форми
        content = request.POST.get('content')
        
        # Отримуємо зображення для публікації з форми
        image = request.FILES.get("image")
        # Формуємо для зображення
        path_to_image = os.path.join("images", "posts", image.name)
        # Створюємо об'єкт файлової системи
        fss = FileSystemStorage()
        # Зберігаємо зображення за вказаним шляхом
        fss.save(name = path_to_image, content = image)

        # Отримуємо користувача, який залогінився
        user = request.user
        # Отримали профіль авторизованного користувача
        profile  = Profile.objects.get(user = user)

        # Отримуємо сиспок усіх тегів з форми
        tags = request.POST.getlist('tags')
        
        # Створюємо об'єк поста у БД
        post = Post.objects.create(
            title = title,
            content = content,
            image = path_to_image,
            author = profile
        )

        # Отримуємо об'єкти тегів за їх id 
        tag_objects = Tag.objects.filter(id__in=tags)
        # зв'язуємо теги з моделлю поста
        post.tags.set(tag_objects)
        # зберігаємо зміни поста
        post.save()
        # перенаправлення на стоірнку усіх постів
        return redirect('all_posts')
        
    
    return render(request=request, template_name='post/create_post.html', context = {'all_tags': all_tags})