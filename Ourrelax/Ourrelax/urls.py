"""Ourrelax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from Ourrelax.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',about),
    path('share/',share),
    path('motivational/',motivational),
    path('morning/',morning),
    path('noon/',noon),
    path('nighty_night/',nighty_night),
    path('before_sleep/',before_sleep),
    re_path(r'new/(?P<id>\d{1,3})',about),
    path('chaxun/',chaxun),
    re_path(r'xiangqinye/(?P<id>\w+)',xiangqinye),
    path('shouye1/',shouye1)
]





from apprelax.views import *
urlpatterns+=[
    path('login/', login),
    path('register/', register),
    path('index/', index),
    path(r'', shouye),
    path('yanqin/',yanqin),
    path('chuanyue/',chuanyue),
    path('xianshi/',xianshi),
    path('riji/',riji),
    path('mypage1/',mypage1),
    path("mypage3/",mypage3),
    path("mypage2/",mypage2),
    path("mypage4/",mypage4),
    re_path("delete/(?P<id>\d{1,3})",delete),
    path('zenjia/',zenjia),
    path('xinzen/',xinzen),
    path('sousuo/', sousuo),
    path('jiancha/',jiancha),
    path('register_student_text/',register_student_text),
    path('logout/', logout),
    re_path(r"sousuo/(?P<word>\w+)", sousuo)

]

