from django.shortcuts import render, redirect
from django.shortcuts import redirect
from django.contrib.auth import logout, login, authenticate

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/anons')
    else:
        return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return redirect('/')