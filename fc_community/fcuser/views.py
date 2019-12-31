from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .forms import LoginForm

def home(request):
    return render(request, 'home.html')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')

def login(request):
    # if request.method == 'GET':
    #     return render(request, 'login.html')
    # elif request.method == 'POST':
    #     username = request.POST.get('username', None)
    #     password = request.POST.get('password', None)

    #     res_data = {}
    #     if not (username and password):
    #         res_data['error'] = 'Fill out all entries'
    #     else: # add no id exception
    #         fcuser = Fcuser.objects.get(username=username) 
    #         if check_password(password, fcuser.password):
    #             request.session['user'] = fcuser.id
    #             return redirect('/')
    #         else:
    #             res_data['error'] = 'Your password is wrong'
    #     return render(request, 'login.html', res_data)

    if request.method == 'POST': 
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else: 
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        useremail = request.POST.get('useremail', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}
        if not (username and useremail and password and re_password):
            res_data['error'] = 'Fill out all entries'
        elif password != re_password:
            res_data['error'] = 'Second password is diffrent from first password'
        else: 
            fcuser = Fcuser(
                username=username, 
                useremail=useremail, 
                password=make_password(password)
            )

            fcuser.save()

        return render(request, 'register.html', res_data)