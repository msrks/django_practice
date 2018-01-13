from django.shortcuts import render

def index(request):
    context = {
        'name': 'msrks'
    }
    return render(request, 'posts/index.html', context)
