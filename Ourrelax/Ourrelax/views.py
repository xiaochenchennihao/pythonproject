from django.shortcuts import render_to_response,render
from django.http import HttpResponse,JsonResponse
from apprelax.models import *
# def index(request):
#     return render_to_response("index.html")





#查询界面中
def mypage(request):
    return render(request, 'mypage2.html')


#缘分享
import random
def share(request):
    a = random.randint(1,10)
    b = random.randint(1,10)
    c = random.randint(1,10)
    article_type1 = Article.objects.filter(type=a)
    article_type2 = Article.objects.filter(type=b)
    article_type3 = Article.objects.filter(type=c)
    article_type = Article.objects.all()
    return render_to_response('share.html',locals())

#早安故事
def morning(request):
    if request.method == "GET":
        page = request.GET.get("page") #获取页码
        page_size = request.GET.get("page_size") #获取每页条数
        if not page: #设置默认页码为1
            page = 1
        if not page_size: #设置默认每页10
            page_size = 10
        page = int(page) #防止url直接传过来字符串的页码
        page_size = int(page_size) #防止url直接传过来字符串的页码
        start = (page-1)*page_size #页码数据开头的索引
        end = page*page_size  #页码数据结尾的索引
    article1 = Article.objects.filter(type=3).order_by("-time")
    article2 = Article.objects.filter(type=6).order_by("-id")
    article =Article.objects.filter(type=2).order_by("id") #排序查询
    lenth = len(article) #获取长度
    page_num = lenth/page_size #计算页码范围
    if page_num != int(page_num): #判断页码是否为整数
        page_num += 1
    page_num = int(page_num)
    page_range = range(1,page_num+1) #页码范围
    data = article[start:end] #截取数据
    return render(request,"morning.html",locals())

#励志故事
def motivational(request):
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
    article1 = Article.objects.filter(type=1).order_by("-time")
    article2 = Article.objects.filter(type=4).order_by("-id")
    article = Article.objects.filter(type=1).order_by("id")  # 排序查询
    lenth = len(article)  # 获取长度
    page_num = lenth / page_size  # 计算页码范围
    if page_num != int(page_num):  # 判断页码是否为整数
        page_num += 1
    page_num = int(page_num)
    page_range = range(1, page_num + 1)  # 页码范围
    data = article[start:end]  # 截取数据
    return render(request, "motivational.html",locals())
#午后故事
def noon(request):
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
    article1 = Article.objects.filter(type=1).order_by("-time")
    article2 = Article.objects.filter(type=8).order_by("-id")
    article = Article.objects.filter(type=3).order_by("id")  # 排序查询
    lenth = len(article)  # 获取长度
    page_num = lenth / page_size  # 计算页码范围
    if page_num != int(page_num):  # 判断页码是否为整数
        page_num += 1
    page_num = int(page_num)
    page_range = range(1, page_num + 1)  # 页码范围
    data = article[start:end]  # 截取数据
    return render(request, "noon.html", locals())

#傍晚故事
def nighty_night(request):
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
    article1 = Article.objects.filter(type=2).order_by("-time")
    article2 = Article.objects.filter(type=6).order_by("-id")
    article = Article.objects.filter(type=5).order_by("id")  # 排序查询
    lenth = len(article)  # 获取长度
    page_num = lenth / page_size  # 计算页码范围
    if page_num != int(page_num):  # 判断页码是否为整数
        page_num += 1
    page_num = int(page_num)
    page_range = range(1, page_num + 1)  # 页码范围
    data = article[start:end]  # 截取数据
    return render(request, "nighty-night.html",locals())
#睡前故事
def before_sleep(request):
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
    article1 = Article.objects.filter(type=4).order_by("-time")
    article2 = Article.objects.filter(type=7).order_by("-id")
    article = Article.objects.filter(type=6).order_by("id")  # 排序查询
    lenth = len(article)  # 获取长度
    page_num = lenth / page_size  # 计算页码范围
    if page_num != int(page_num):  # 判断页码是否为整数
        page_num += 1
    page_num = int(page_num)
    page_range = range(1, page_num + 1)  # 页码范围
    data = article[start:end]  # 截取数据
    return render(request, "before_sleep.html",locals())

#言情小说
def yanqin(request):
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
    article1 = Article.objects.filter(type=3).order_by("-time")
    article2 = Article.objects.filter(type=5).order_by("-id")
    article = Article.objects.filter(type=7).order_by("id")  # 排序查询
    lenth = len(article)  # 获取长度
    page_num = lenth / page_size  # 计算页码范围
    if page_num != int(page_num):  # 判断页码是否为整数
        page_num += 1
    page_num = int(page_num)
    page_range = range(1, page_num + 1)  # 页码范围
    data = article[start:end]  # 截取数据
    return render(request, "yanqin.html",locals())
#穿越小说
def chuanyue(request):
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
    article1 = Article.objects.filter(type=2).order_by("-time")
    article2 = Article.objects.filter(type=4).order_by("-id")
    article = Article.objects.filter(type=8).order_by("id")  # 排序查询
    lenth = len(article)  # 获取长度
    page_num = lenth / page_size  # 计算页码范围
    if page_num != int(page_num):  # 判断页码是否为整数
        page_num += 1
    page_num = int(page_num)
    page_range = range(1, page_num + 1)  # 页码范围
    data = article[start:end]  # 截取数据
    return render(request, "chuanyue.html", locals())
#现实小说
def xianshi(request):
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
    article1 = Article.objects.filter(type=1).order_by("-time")
    article2 = Article.objects.filter(type=8).order_by("-id")
    article = Article.objects.filter(type=9).order_by("id")  # 排序查询
    lenth = len(article)  # 获取长度
    page_num = lenth / page_size  # 计算页码范围
    if page_num != int(page_num):  # 判断页码是否为整数
        page_num += 1
    page_num = int(page_num)
    page_range = range(1, page_num + 1)  # 页码范围
    data = article[start:end]  # 截取数据
    return render(request, "xianshi.html",locals())
#日记类型
def riji(request):
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
    article1 = Article.objects.filter(type=1).order_by("-time")
    article2 = Article.objects.filter(type=8).order_by("-id")
    article = Article.objects.filter(type=10).order_by("id")  # 排序查询
    lenth = len(article)  # 获取长度
    page_num = lenth / page_size  # 计算页码范围
    if page_num != int(page_num):  # 判断页码是否为整数
        page_num += 1
    page_num = int(page_num)
    page_range = range(1, page_num + 1)  # 页码范围
    data = article[start:end]  # 截取数据
    return render(request, "riji.html",locals())


#点击书进入书页时的操作
#详情页
def about(request,id):
    id = int(id)
    article = Article.objects.get(id = id)
    if request.POST:
        a = comment()
        text = request.POST.get("text")
        a.Text = text
        a.save()
    comments = comment.objects.all()
    return render(request,'about.html',locals())

#查询 分页
def chaxun(request):
    if request.method == "GET":
        page = request.GET.get("page")
        page_size = request.GET.get("page_size")
        onece_page = 5
        if not page:
            page = 1
        if not page_size:
            page_size = 10
        page = int(page)
        page_size = int(page_size)
        if page % onece_page == 0:
            s_n = int(page / onece_page)
            r_n = onece_page
        else:
            s_n = int(page / onece_page) + 1
            r_n = page % onece_page
        total = Article.objects.filter().order_by("id")  # 查询所有的数据

        select_start = (s_n - 1) * onece_page * page_size
        select_end = s_n * onece_page * page_size
        select_range = total[select_start:select_end]
        return_start = (r_n - 1) * page_size
        return_end = r_n * page_size
        return_range = select_range[return_start:return_end]

        if page <= 3:
            page_range = range(1, 6)
        else:
            page_range = range(page - 2, page + 3)
        return_list = []
        for data in return_range:
            if data.picture:
                pic = data.picture.url.replace('/media','')
                print(pic)
            else:
                pic = "None"
            return_list.append({
                "id": data.id,
                "title": data.title,
                # "author": data.author,
                "time": data.time,
                "description": data.description,
                "content": data.content,
                "picture": pic,
                # 'type':data.type

            })
        result = {"data": return_list, "page_range": ",".join([str(i) for i in page_range])}
        return JsonResponse(result)

    return render(request,"chaxun.html")








#我们的分页显示
def mypage1(request):
    if request.method == "GET":
        page = request.GET.get("page")
        page_size = request.GET.get("page_size")
        onece_page = 5
        if not page:
            page = 1
        if not page_size:
            page_size = 5
        page = int(page)
        page_size =int(page_size)
        if page % onece_page == 0:
            s_n = int(page / onece_page)
            r_n = onece_page
        else:
            s_n = int(page / onece_page) + 1
            r_n = page % onece_page
        total = Article.objects.all()  # 查询所有的数据

        select_start = (s_n - 1) * onece_page*page_size
        select_end = s_n * onece_page*page_size
        select_range = total[select_start:select_end]
        return_start = (r_n - 1) * page_size
        return_end = r_n * page_size
        return_range = select_range[return_start:return_end]

        if page <= 3:
            page_range = range(1, 6)
        else:
            page_range = range(page - 2, page + 3)
        return_list = []
        for data in return_range:
            if data.picture:
                pic = data.picture.url
            else:
                pic = "None"
            return_list.append({
                "id":data.id,
                "title":data.title,
                # "author": data.author,
                "time": data.time,
                "description": data.description,
                "content": data.content,
                # "picture": data.picture,
                # 'type':data.type

            })
        result = {"data":return_list,"page_range":",".join([str(i) for i in page_range])}
        return JsonResponse(result)
#倒叙查询
def mypage3(request):
    if request.method == "GET":
        page = request.GET.get("page")
        page_size = request.GET.get("page_size")
        onece_page = 5
        if not page:
            page = 1
        if not page_size:
            page_size = 5
        page = int(page)
        page_size =int(page_size)
        if page % onece_page == 0:
            s_n = int(page / onece_page)
            r_n = onece_page
        else:
            s_n = int(page / onece_page) + 1
            r_n = page % onece_page
        total = Article.objects.order_by("-time")  # 查询所有的数据

        select_start = (s_n - 1) * onece_page*page_size
        select_end = s_n * onece_page*page_size
        select_range = total[select_start:select_end]
        return_start = (r_n - 1) * page_size
        return_end = r_n * page_size
        return_range = select_range[return_start:return_end]

        if page <= 3:
            page_range = range(1, 6)
        else:
            page_range = range(page - 2, page + 3)
        return_list = []
        for data in return_range:
            if data.picture:
                pic = data.picture.url
            else:
                pic = "None"
            return_list.append({
                "id":data.id,
                "title":data.title,
                # "author": data.author,
                "time": data.time,
                "description": data.description,
                "content": data.content,
                # "picture": data.picture,
                # 'type':data.type

            })
        result = {"data":return_list,"page_range":",".join([str(i) for i in page_range])}
        return JsonResponse(result)
def mypage2(request):
    a = range(10)
    return render(request,"mypage2.html",locals())
def mypage4(request):
    a = range(10)
    return render(request,"mypage4.html",locals())
#新增函数
import random
def xinzen(request):
    return render(request,'xinzen.html')
def zenjia(request):
    result = {"state":"error","data":""}
    if request.method=="POST" and request.POST:
        data = request.POST
        title = data.get("title")
        typef = data.get("type")
        time = data.get("time")
        description = data.get("description")
        content = data.get("content")
        img = request.FILES.get("pic")
        type1 = Type.objects.get(label=typef)

        a = Article()
        a.title = title
        a.time = time
        a.description = description
        a.content = content
        a.author = Author.objects.get(name = "佚名")
        a.picture = img
        a.save()
        a.type.add(type1)


        result["state"] = "success"
        result["data"] = "save data success"
    else:
        result["data"] = "request method must be post and post not be null"
    return JsonResponse(result)




#在程序中添加作品函数，没事不要用
def register_student_text(request):
    for i in range(30):
        title = random.choice(["时光","巴黎圣母院"])
        time = random.choice(['1970-1-1','2015-2-1','2019-2-1','2019-1-9'])
        description = random.choice(["一段美丽而优雅的文字","一段让人同侧心扉的文字"])
        content = random.choice(["测试1","测试2"])
        author = Author.objects.get(name="佚名")
        type = random.choice(Type.objects.all())
        s = Article()
        s.title = title
        s.time = time
        s.description = description
        s.content = content
        s.author = author
        s.save()
        s.type.add(type)
    return render(request,"chaxun.html",locals())

def xiangqinye(request,id):

    return render(request,'xiangqinye.html',locals())

def shouye1(request):
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
    return render(request,'shouye1.html',locals())

