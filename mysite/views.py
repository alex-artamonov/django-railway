from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("<strong>hi from Django</strong>")