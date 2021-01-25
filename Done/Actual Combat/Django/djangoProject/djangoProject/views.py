from django.http import HttpResponse


def hello_idex(request):
    return HttpResponse('Hello world')