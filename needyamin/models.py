from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import strip_tags

from django.contrib.auth.models import User
from PIL import Image

#python manage.py makemigrations
#python manage.py migrate
#python manage.py runserver

class User(AbstractUser):
    pass

def user_directory_path(instance, image):
    return 'blog_image/user_{0}/{1}'.format(instance.user.id, image)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name="user")
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=1000, null=True, blank=True)
    username = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to = user_directory_path)
    contents = models.TextField(max_length=5000, default='Empty')
    date = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=200, null=True, blank=True)
    ip = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, default='0')
    
    def __str__(self):
        return f"{self.id} {self.title} | IP: {self.ip} | date: {self.date}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # saving image first

        image = Image.open(self.image.path) # Open image using self

        if image.height > 300 or image.width > 300:
            new_img = (300, 300)
            image.thumbnail(new_img)
            image.save(self.image.path)  # saving image at the same path
            

class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    ip = models.CharField(max_length=200, null=True, blank=True)
    time_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{strip_tags(self.comment[0:10])}... by {self.user.username} at {self.time_posted}"



class contactus(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    content = models.CharField(max_length=1200)

    def __str__(self):
        return f"Name: {self.name} || Email: {self.email}"

class Email_Subscription(models.Model):
    ip = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.email}"

def favourite_icon(instance, image):
    return 'blog_image/user_{0}/{1}'.format(instance.user.id, image)

class SiteConfig(models.Model):
    title = models.CharField(max_length=2000,null=True, blank=True)
    description = models.TextField(max_length=2000,null=True, blank=True)
    favourite_icon = models.ImageField(upload_to ='favourite_icon/', null=True, blank=True)
    keywords = models.CharField(max_length=2000,null=True, blank=True)
    script_add = models.CharField(max_length=5000,null=True, blank=True)
    privacy = models.TextField(max_length=5000,null=True, blank=True)
    aboutus = models.TextField(max_length=2000,null=True, blank=True)
    
    def __str__(self):
        return f"{self.id} {self.title} {self.description}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # saving image first

        favourite_icon = Image.open(self.favourite_icon.path) # Open image using self

        if favourite_icon.height > 300 or favourite_icon.width > 300:
            new_img = (16, 16)
            favourite_icon.thumbnail(new_img)
            favourite_icon.save(self.favourite_icon.path)  # saving image at the same path