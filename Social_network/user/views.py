from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError 
from django.contrib.auth import authenticate, login, logout
from .models import Profile


def render_registration(request):
    # Змінні, що відповідають за навність помилки. Ці змінні будуть передані у шаблон
    show_text_passwords_dont_match = False
    show_text_not_unique_name = False
    # Якщо метод запиту POST (Якщо користувач надсилає форму)
    if request.method == "POST":
        # Отримуємо дані з форми і зберігаємо у змінні
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm-password")
        # Якщо користувач підтвердив пароль
        if password == confirm_password: 
            # Відловлюємо помилку, якщо користувач реєструться під вже існуючим юзернеймом
            try:
                # Створюємо об'єкт юзера і зберігаємо у БД
                User.objects.create_user(username = username, password = password)
                # Перенаправляємо користувача на сторінку login
                return redirect("login")
            except IntegrityError:
                show_text_not_unique_name = True
        else: 
            show_text_passwords_dont_match = True     
    return render(
        request= request, 
        template_name= "user/registration.html", 
        context = {
            'show_text_passwords_dont_match': show_text_passwords_dont_match,
            "show_text_not_unique_name": show_text_not_unique_name
            }
    )

def render_login(request):
    user = True
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Перевіряє наявність користувача у БД за вказаними юзернеймом та паролем. 
        # Якщо користувач існує, повертає об'єкт користувача. 
        # Якщо не існує - повертає None
        user = authenticate(request, username = username, password = password)
        # Якщо user не порожній (користувач ввів дані вірно)
        if user:
            # Авторизуємо користувача
            login(request, user)
            # Перенаправляємо на сторінку "Welcome"
            return redirect('welcome') 
    return render(request=request, template_name="user/login.html", context= {"user":user})


def welcome(request):
    # Якщо користувач залогінився
    if request.user.is_authenticated:
        return render(request, "user/welcome.html")
    else:
        return redirect("login")
    
    
def logout_user(request):
    # Вихід з акаунту
    logout(request)
    return redirect('login')
    
def render_all_profiles(request):
    all_profiles = Profile.objects.all()
    return render(request, 'user/all_profiles.html' ,context={'all_profiles':all_profiles})