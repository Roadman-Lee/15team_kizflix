from django.shortcuts import render, redirect
from .models import UserModel, UserLikes, UserProfiles
from contents.models import PostModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model  # 사용자가 데이터베이스 안에 있는지 검사하는 함수
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

        if password != password2:
            return render(request, 'users/signup.html')

        else:
            exist_user = get_user_model().objects.filter(username=username)

            if exist_user:
                return render(request, 'users/signup.html')

            else:
                UserModel.objects.create_user(
                    username=username, password=password, nickname=nickname, email=email)
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


@login_required  # 사용자가 로그인이 되어 있어야 만 접근할 수 있는 함수
def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required
def like_post(request, id):
    if request.method == 'GET':
        user = request.user.is_authenticated
        # 01. 내가 좋아요한 리스트
        dblikes = []
        if user:
            # 02. 로그인한 유저가 좋아요한 포스트 가져오기
            if UserLikes is not None:
                likes_postlist = UserLikes.objects.filter(user_id=id)

                for post in likes_postlist:
                    dblikes.append(post.post_id.post_id)  # post_id를 출력

                return render(request, 'users/mypage.html', {'dblikes': dblikes})


@login_required
def profile(request):
    # 01. user의 profile 가져오기
    # 02. profile의 pf_image 바꾸기
    return
