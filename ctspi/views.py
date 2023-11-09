from os import name
from django.shortcuts import render
from .models import Main_contents


def main(request):
    name = request.path_info[1:]
    if not name:
        name = 'main'
    try:
        post = Main_contents.objects.get(name=name)
    except:
        return render(request, '404.html', status=404, context={'name': name})

    context = {'post': post, 'assa': 'assa'}
    return render(request, 'index.html', context)
