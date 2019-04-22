from django.contrib import admin
from django.contrib import admin
from apprelax.models import Article,Author,Message,Type,Picture,people_user

admin.site.register(Article) #注册
admin.site.register(Author) #注册
admin.site.register(Message) #注册
admin.site.register(Type) #注册
admin.site.register(Picture) #注册
admin.site.register(people_user)#注册

# Register your models here.
