from django.shortcuts import render, redirect
from .models import Main_contents, Department
from ctspi_config.settings import STATIC_ROOT, BASE_DIR
import re

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

def save_to_csv(request):
    with open(f"{BASE_DIR}{STATIC_ROOT}titl.csv", 'w', encoding='utf-8') as f:
        f.write(f"  {str.replace(request.GET['title'],';','    ;   ')}".rstrip())
    return redirect('https://ctspi.e0m.ru/static/html/ttt.html')

def save_to_txt(request):
    with open(f"{BASE_DIR}config.txt", 'w', encoding='utf-8') as f:
        try:
            f.write(request.POST['anons'])
        except:
            pass
    return render(request, 'anons.html', context={'r': request, })
