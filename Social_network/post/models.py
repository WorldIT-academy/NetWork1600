from django.db import models
from user.models import Profile


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    icon = models.ImageField(upload_to= "images/tag_icons", blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)
    

    def __str__(self):
        return  self.name
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to= "images/posts")
    author = models.ForeignKey(Profile, on_delete= models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    
    

    