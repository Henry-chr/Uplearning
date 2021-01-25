from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello World !")

def runoob(request):
    context = ['菜鸟教程1','菜鸟教程2','菜鸟教程3','菜鸟教程4',]
    # context['hello'] = 'Hello world !'
    return render(request,'runoob.html',{"context":context})
def run(request):
    view_name = {"name":'陈浩然'}
    return render(request,'run.html',{"view_name":view_name})
