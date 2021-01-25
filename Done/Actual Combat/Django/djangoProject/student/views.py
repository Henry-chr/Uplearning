# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
# 处理登录功能
def logon_view(request):
    # 接收表单请求参数
    uname = request.POST.get('uname')
    pwd = request.POST.get('pwd')

    print(uname,pwd)

    #判断是否登录成功
    if uname == 'chr' and pwd == 'chr465521':
        return HttpResponse('登录成功')
    return HttpResponse('登录失败')

# 渲染登录首页
def index_view(request):
    return render(request,'logon.html')


def register_view(request):
    method = request.method
    print(method)
    if method == 'GET':
        return render(request,'register.html')
    else:
        # 获取请求参数
        sname = request.POST.get('uname')
        spwd = request.POST.get('pwd')

        # 判断
        if sname and spwd:
        #     创建模型对象
            stu = pp_logon_user(user_name=sname,user_pwd=spwd)
        #     插入数据库
            stu.save()
            return HttpResponse("注册成功")
        return HttpResponse("注册失败")


def edslogon_view(request):
    sname = request.GET.get('sname')
    sid = request.GET.get('sid')
    spwd = request.GET.get('spwd')
    smail = request.GET.get('smail')
    # 判断
    print(sname,sid,spwd,smail)
    if sname and spwd and sid and smail:
        #     创建模型对象
        autologon = pp_autologon_test(user_name=sname,user_id=sid,user_pwd=spwd,user_mail=smail)
        #     插入数据库
        autologon.save()
        print('注册成功')
        return HttpResponse('注册成功')
    else:
        print('注册失败')
        return HttpResponse('注册失败')


def show_view(request):
    data = pp_logon_user.objects.all()
    return render(request,'show.html',{'data':data})

def ybjs_test(request):
    return render(request,'text.html')