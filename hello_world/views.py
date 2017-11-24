# helloworld_project/views.py
from django.http import HttpResponse


def home_page(request):
    return HttpResponse("Hello, world!")