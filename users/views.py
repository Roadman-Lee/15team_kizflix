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
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        password2 = request.POST.get('password2','')
        nickname = request.POST.get('nickname','')
        email = request.POST.get('email','')


        if password != password2:
            return render(request, 'users/signup.html', {'error': '패스워드를 확인해주세요'})

        else:
            if username == '' or password == '':
                return render(request, 'user/signup.html', {'error': '사용자 이름과 비밀번호는 필수 값 입니다'})
            exist_user = get_user_model().objects.filter(username=username)

            if exist_user:
                return render(request, 'users/signup.html', {'error': '사용자가 이미 존재합니다'})

            else:
                user = UserModel.objects.create_user(username=username, password=password, nickname=nickname, email=email)

                profile = UserProfiles(user=user)
                profile.save()

                return render(request, 'users/signin.html')


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)

        if me is not None:
            auth.login(request, me)
            return redirect('/')
            # return HttpResponse(me.username)
        else:
            return render(request, 'users/signin.html', {'error': '유저이름 혹은 패스워드를 확인 해 주세요'})

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
def profile(request, id):
    user = request.user.is_authenticated
    if user:
        user_exist = UserModel.objects.get(username=request.user)
        profile = UserProfiles.objects.get(user=user_exist)
        if request.method == 'POST':
            # 클라이언트에서 서버로 수정할 프로필 정보 전달
            pf_Edit = request.POST.get('profile_img')
            print(pf_Edit)
            # UPDATE
            profile.pf_image = pf_Edit
            profile.save()
            return redirect('/mypage/'+str(id))

        elif request.method == 'GET':
            # 01. 빈 리스트 만들기
            dblikes = []
            if UserLikes is not None:
                likes_postlist = UserLikes.objects.filter(user_id=request.user).order_by('-created_at')
                for post in likes_postlist:
                    dblikes.append(PostModel.objects.filter(post_id=post.post_id_id))



                    # dblikes.append(PostModel.objects.filter(post_id=post.post_id_id).values())

            return render(request, 'users/mypage.html', {'profile':profile, 'dblikes':dblikes})
    else:
        return render(request, 'user/signin.html')
    # 02. profile의 pf_image 바꾸기

# def profileEdit(request,id):
#     user = request.user.is_authenticated
#     if request.method == 'POST':
#         if user:
#             # 클라이언트에서 서버로 수정할 프로필 정보 전달
#             pf_Edit = request.POST.get['pf_Edit']
#             # UPDATE
#             user_exist = UserModel.objects.get(username=request.user)
#             profile = UserProfiles.objects.get(user=user_exist)
#             profile.pf_image = pf_Edit
#             profile.save()
#

