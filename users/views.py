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

                user_id = UserModel.objects.create_user(username=username, password=password, nickname=nickname, email=email)
                user_id.save()
                profile = UserProfiles(user_id=user_id)
                profile.save()

                return render(request, 'users/signin.html')


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
    return redirect('/sign-in')



@login_required
def like_post(request,id):
    if request.method == 'GET':
        user = request.user.is_authenticated
        # 01. 빈 리스트 만들기
        dblikes = []
        if user:
            # 02. userid가 일치하는 likes db 가져오기'
            if UserLikes is not None:
                likes_postlist = UserLikes.objects.filter(user_id=request.user).order_by('-created_at')
                print(likes_postlist)
                for post in likes_postlist:
                    dblikes.append(PostModel.objects.filter(post_id=post.post_id_id))
                    # dblikes.append(PostModel.objects.filter(post_id=post.post_id_id).values())
                return render(request, 'users/mypage.html', {'dblikes':dblikes })
        else :
            return render(request, 'user/signin.html')


@login_required
def profile(request):
    # 01. user의 profile 가져오기
    # 02. profile의 pf_image 바꾸기
    return
