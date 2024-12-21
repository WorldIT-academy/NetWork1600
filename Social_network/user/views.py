from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError 
from django.contrib.auth import authenticate, login


def render_registration(request):
    show_text_passwords_dont_match = False
    show_text_not_unique_name = False
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm-password")
        if password == confirm_password: 
            try:
                User.objects.create_user(username = username, password = password)
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
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            return redirect('welcome')
            
        
    return render(request=request, template_name="user/login.html")


def welcome(request):
    return render(request, "user/welcome.html")
    
