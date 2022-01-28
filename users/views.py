from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model # 사용자가 데이터베이스 안에 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'users/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        nickname = request.POST.get('nickname', None)
        email = request.POST.get('email', None)

        if password != password2 :
            return render(request, 'users/signup.html')


        else :
            exist_user = get_user_model().objects.filter(username=username)

            if exist_user :
                return render(request, 'users/signup.html')

            else :
                UserModel.objects.create_user(username=username, password=password, nickname=nickname, email=email)
                return redirect('/sign-in')

def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/')
             # return HttpResponse(me.username)
        else:
            return redirect('sign-in')

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'users/signin.html')

@login_required #사용자가 로그인이 되어 있어야 만 접근할 수 있는 함수
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def like_post(request):

    return

@login_required
def profile(request):
    return

