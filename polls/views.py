from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. 73b20480 You're at the polls index.")