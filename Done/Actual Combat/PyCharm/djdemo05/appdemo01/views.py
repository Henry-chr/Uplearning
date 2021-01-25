from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
#业务逻辑代码

def test_view(request):
    print("测试连接"+str(request))
    print(dir(request))
    return HttpResponse("测试成功")

def login_view(request):
    html = """
    <form>
        <input type="text" name="username">
        <br>
        <input type="password" name="password">
        <br>
        <input type="submit" value="提交">
    </form>
    """
    return HttpResponse(html)

def test_2003(request):
    return HttpResponse('test_2003')

def test_archive(request,year):
    return HttpResponse('test_archive   动态   %s' % year )