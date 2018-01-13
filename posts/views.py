from django.shortcuts import render

def index(request):
    context = {
        'name': 'msrks'
    }
    return render(request, 'posts/index.html', context)

def about(request):
    return render(request, 'posts/about.html')

def info(request):
    return render(request, 'posts/info.html')
