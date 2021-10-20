from django.db import models

# Create your models here.

from django.db.models.deletion import CASCADE

#Home sections

class Home(models.Model):
    name = models.CharField(max_length=200)
    greeting_1 = models.CharField(max_length=200)
    greeting_2 = models.CharField(max_length=200)
    #save time when modified
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
#ShOWS

class Show(models.Model):
    name = models.CharField(max_length=200)
    venue  = models.CharField(max_length=200)
    Date  = models.CharField(max_length=200)
    Time  = models.CharField(max_length=6)
    link = models.URLField(max_length=1000)
    updated  = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
#show1 for second program 
class Show1(models.Model):
    name = models.CharField(max_length=200)
    venue  = models.CharField(max_length=200)
    Date  = models.CharField(max_length=200)
    Time  = models.CharField(max_length=6)
    link = models.URLField(max_length=1000)
    updated  = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

#big hitters picture weekly change
# class BigHitters(models.Model):
#     picture = models.ImageField(upload_to = 'picture/')
#     artiste_name = models.CharField(max_length=200)
#     updated  = models.DateTimeField(auto_now=True)
    
    
#     def __str__(self):
#         return self.artiste_name   

class YouTube(models.Model):
    name = models.CharField(max_length=200)
    VideoId = models.CharField(max_length=200)
    updated  = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class YouTubesecond(models.Model):
    updated  = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    vidId = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
# #news hero picture
# class heropic(models.Model):
#     image  = models.ImageField(upload_to = "pictures")