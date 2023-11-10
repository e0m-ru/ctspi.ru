from os import name
from django.shortcuts import render
from .models import Main_contents, Department


def main(request):
    url_path = request.path
    context = {'items': Main_contents.objects.all()}
    if url_path == '/':
        url_path = '/main'
    if url_path == '/departments':
        context.update({'depts': Department.objects.all()})
    try:
        post = Main_contents.objects.get(name=url_path[1:])
    except:
        return ctspi_404(request)
    context.update({'post': post})
    return render(request, 'index.html', context)


def departments(request):
    try:
        post = Department.objects.get(name=request.path.split('/')[-1])
    except:
        return ctspi_404(request)
    return render(request, 'index.html', context={'r': request, 'post': post, 'depts': Department.objects.all(), 'items': Main_contents.objects.all()})


def ctspi_404(request):
    return render(request, '404.html', status=404, context={'name': request.path})
