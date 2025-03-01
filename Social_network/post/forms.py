from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__" 

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name[0].isalpha():
            raise ValidationError('Назва тегу повинна починатись тільки з літери')
        return name


        


# Створюємо клас для форми
class PostForm(forms.ModelForm):
    # Клас, що відповідає за налаштування форми
    class Meta:
        # Підв'язуємо модель до форми
        model = Post
        # Вказуємо поля, які мають відображатись на сторінці
        fields = ["title", "content", "image", "tags",]
        # Кастомізацій полів (вказуємо типи полів та їх атрибути)
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-input", "placeholder": "Заголовок"}),
            "content": forms.Textarea(attrs={"placeholder": "content"}),       
        }
    # Переазписуємо метод save
    def save(self, author_profile):
        # Створюємо об'єкт поста за допомогою методу save з батьківського класу,
        # проте не зберігаємо у БД (за це відповідає commit = False))
        post = super().save(commit = False)
        # Підв'язуємо автора до поста та зберігаємо зміни
        post.author = author_profile
        post.save()
        # Підв'язуємо теги до поста та зберігаємо зміни
        post.tags.set(self.cleaned_data.get("tags"))
        post.save()

    
