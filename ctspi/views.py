from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Main_contents, Department
from ctspi_config.settings import STATIC_ROOT, BASE_DIR
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

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
        pass
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


@login_required(login_url="/login/")
def anons(request):
    context = {'items': Main_contents.objects.all()}
    return render(request, 'anons.html', context=context)

def write_anons(request):
    with open(f'{BASE_DIR}/static/anons.csv', 'w', encoding='utf-8') as file:
        file.write(resp:=str(request.body.decode('utf-8')))
    # Создаем свой кастомный ответ
    custom_response = HttpResponse(resp, content_type="text/plain")
    custom_response.status_code = 200
    return custom_response
