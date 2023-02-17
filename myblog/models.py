from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    header_image=models.ImageField(null=True,blank=True,upload_to="images/")
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    # body=models.TextField()
    body=RichTextField(blank=True,null=True)
    post_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=252,default='Sports')
    snippet=models.CharField(max_length=130)
    like= models.ManyToManyField(User,related_name="blog_posts")

    def total_likes(self):
        return self.like.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse("home")
    

class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("home")
    
class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    profile_pic=models.ImageField(null=True,blank=True,upload_to="images/profile/")
    website_url=models.CharField(max_length=255,null=True,blank=True)
    fb_url=models.CharField(max_length=255,null=True,blank=True)
    insta_url=models.CharField(max_length=255,null=True,blank=True)
    linkedin_url=models.CharField(max_length=255,null=True,blank=True)
    bio=models.TextField()

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("home")


class Comment(models.Model):
    post=models.ForeignKey(Post,related_name="comments", on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    body=models.TextField()
    date_added=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    