from django.db import models

class comment(models.Model):
    Text = models.TextField()
    def __str__(self):
        return self.Text


class Type(models.Model):
    label = models.CharField(max_length = 32)#lable char(30)
    description = models.TextField()
    def __str__(self):
        return self.label

class Author(models.Model):
    name = models.CharField(max_length = 32,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    birthday = models.DateField(verbose_name='生日')
    email = models.EmailField(verbose_name='email')
    phone = models.CharField(max_length = 32,verbose_name='电话')
    photo = models.ImageField(upload_to = "images",verbose_name='图片')
    address = models.TextField(verbose_name='地址')
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length = 32,verbose_name="题目")
    author = models.ForeignKey(to = Author,on_delete = models.CASCADE,verbose_name="作者")
    time = models.DateField(verbose_name="日期")
    description = models.TextField(verbose_name="简介")
    content = models.TextField(verbose_name="内容")
    picture = models.ImageField(upload_to = "images",verbose_name="图片",blank=True,null=True)
    type = models.ManyToManyField(to = Type,verbose_name="类型")
    def __str__(self):
        return self.title
class Picture(models.Model):
    label = models.CharField(max_length = 32)
    image = models.ImageField(upload_to = "images")
    def __str__(self):
        return self.label

class Message(models.Model):
    content = models.TextField()
    time = models.DateTimeField()
    messager = models.CharField(max_length = 32)
    def __str__(self):
        return self.content
class people_user(models.Model):
    username = models.CharField(max_length = 32)
    password = models.CharField(max_length = 32)
    user_email = models.EmailField()
    def __str__(self):
        return self.username

# Create your models here.
