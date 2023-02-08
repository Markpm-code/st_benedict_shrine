from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def our_story(request):
    return render(request, 'our_story.html')


def gallery(request):
    return render(request, 'gallery.html') 


def services(request):
    return render(request, 'services.html')      