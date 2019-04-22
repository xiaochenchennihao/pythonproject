from django.shortcuts import render
from django.shortcuts import render,render_to_response
import hashlib
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect #跳转页面
from apprelax.models import *
def shouye(request):
    if request.method == "GET":
        page = request.GET.get("page")  # 获取页码
        page_size = request.GET.get("page_size")  # 获取每页条数
        if not page:  # 设置默认页码为1
            page = 1
        if not page_size:  # 设置默认每页10
            page_size = 10
        page = int(page)  # 防止url直接传过来字符串的页码
        page_size = int(page_size)  # 防止url直接传过来字符串的页码
        start = (page - 1) * page_size  # 页码数据开头的索引
        end = page * page_size  # 页码数据结尾的索引
    article = Article.objects.all().order_by("-time")  # 排序查询
    lenth = len(article)  # 获取长度
    page_num = lenth / page_size  # 计算页码范围
    if page_num != int(page_num):  # 判断页码是否为整数
        page_num += 1
    page_num = int(page_num)
    page_range = range(1, page_num + 1)  # 页码范围
    data = article[start:end]  # 截取数据
    article_type = Article.objects.all()
    #上面是分页程序
    return render(request, "shouye.html", locals())

def logout(request):
    response = HttpResponseRedirect("/login")
    response.delete_cookie("username")
    return response

#首页
def userValid(fun):
    def inner(request,*args,**kwargs):
        username = request.COOKIES.get("username")
        if username:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/login/")
    return inner
@userValid
def index(request):
    if request.method == "GET":
        page = request.GET.get("page")  # 获取页码
        page_size = request.GET.get("page_size")  # 获取每页条数
        if not page:  # 设置默认页码为1
            page = 1
        if not page_size:  # 设置默认每页10
            page_size = 10
        page = int(page)  # 防止url直接传过来字符串的页码
        page_size = int(page_size)  # 防止url直接传过来字符串的页码
        start = (page - 1) * page_size  # 页码数据开头的索引
        end = page * page_size  # 页码数据结尾的索引
    article = Article.objects.all().order_by("-time")  # 排序查询
    lenth = len(article)  # 获取长度
    page_num = lenth / page_size  # 计算页码范围
    if page_num != int(page_num):  # 判断页码是否为整数
        page_num += 1
    page_num = int(page_num)
    page_range = range(1, page_num + 1)  # 页码范围
    data = article[start:end]  # 截取数据
    article_type = Article.objects.all()
    #上面是分页程序
    return render(request, "index.html", locals())

#可以进行模糊搜索的搜索框
import random
def sousuo(request,word):
        article1 = Article.objects.all()[:7]
        article = Article.objects.filter(title__icontains=word)
        return render(request,"liebiaoye.html",locals())

#注册
def register(request):
    if request.method == "POST" and request.POST:
        data = request.POST
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        people_user.objects.create(
            username = username,
            password = setPassword(password),
            user_email = email
        )
        return HttpResponseRedirect("/login")
    return render(request,"register.html")

def jiancha(request):
    result = {"state": "error", "data": ""}
    if request.method == "POST" and request.POST:
        email = request.POST.get("email")
        a = people_user.objects.filter(user_email=email)
        if a:
            result["state"] = "success"
            result["data"] = "邮箱已存在！请重新选择新的邮箱！"
        else:
            result["data"] = "检测到邮箱可以使用"

    return JsonResponse(result)
#登录界面
def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    password = md5.hexdigest()
    return str(password)

def login(request):
    if request.method == "POST" and request.POST:
        user_email = request.POST.get("email")
        password = request.POST.get("password")

        e = people_user.objects.filter(user_email = user_email).first()
        print(e)
        if e:
            now_password = setPassword(password)
            db_password = e.password
            if now_password == db_password:

                response = HttpResponseRedirect("/index/")
                response.set_cookie("username",e.username)
                return response

    return render(request,"login.html")
#删除界面
def delete(request,id):
    page = int(id)
    article = Article.objects.filter(id = page)
    article.delete()
    return render_to_response('mypage2.html',locals())


# def logout(request):
#     response = HttpResponseRedirect("/login/")
#     response.delete_cookie("username")
#     return response

# Create your views here.
# Create your views here.
#公共分页界面
