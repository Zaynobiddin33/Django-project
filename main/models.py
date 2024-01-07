from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    text = models.TextField()
    author = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = "portfolio"

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(null = True, max_length=13,)
    message = models.TextField()

    def __str__(self):
        return self.email

class Service(models.Model):
    title = models.CharField(max_length = 255)
    info = models.TextField()
    icon = models.ImageField()

    def __str__(self) -> str:
        return self.title

class About(models.Model):
    # time = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255)
    info = models.TextField()
    picture = models.ImageField()

    class Meta:
        verbose_name = 'Data'
        verbose_name_plural = 'About us'

    def __str__(self) -> str:
        return self.title

class Team(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length = 255)
    role = models.CharField(max_length = 255)
    twitter = models.URLField()
    linkedin = models.URLField()
    facebook = models.URLField()

    def __str__(self):
        return self.name


