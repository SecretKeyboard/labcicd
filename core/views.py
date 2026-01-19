from django.http import HttpResponse


def home(request):
    return HttpResponse("Core app is working!")
