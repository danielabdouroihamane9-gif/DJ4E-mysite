from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. 8acd091f You're at the polls index.")