from django.http import HttpResponse


# Basic URL page that prints "hello world"
def index(request):
    return HttpResponse("Hello, world. You're at the tickets index.")