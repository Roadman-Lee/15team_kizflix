
from django.shortcuts import render, redirect
from users.models import UserModel, UserLikes, UserProfiles
from .models import PostModel

# Create your views here.


def category_view(request, slug):

    user = request.user.is_authenticated
    if request.method == 'GET':
        if user:

            # 1. pk별 카테고리 포스트 받아오기

            category_post = PostModel.objects.filter(post_category=slug)
            return render(request, 'contents/category.html', {'post_list': category_post})
        else:
            return render(request, 'user/signin.html')


def detail_view(request, id):
    user = request.user.is_authenticated
    if user:
        post_id_recieve = request.POST.get('post_give')
        if request.method == 'GET':
            post = PostModel.objects.get(post_id=post_id_recieve)

            return render(request, 'contets/detail.html', {'post': post})

            # recommanded_contents = UserModel.objects.get(id=id)  all에서 추천된 컨텐츠가 저장되어있는 db로 바꿔야함
            # return render(request, 'contents/detail.html', {'re_contents': recommanded_contents})

        if request.method == 'POST':

            # 정보 불러오기
            like_recieve = request.POST.get('like_give')
            # 1 : 좋아요 0 : 좋아요 취소

            user_exist = UserModel.objects.get(username=request.user)

            if like_recieve == 1:
                # like에 user, post 정보 저장
                like_post = UserLikes(user_id=user_exist,
                                      post_id=post_id_recieve)
                like_post.save()

                # post의 like_count 업데이트 like_count += 1
                post_id = PostModel.objects.filter(post_id=post_id_recieve)
                count = post_id.like_count + 1
                post_id.update(like_count=count)

            else:
                # user, post정보와 일치하는 like정보 삭제
                like_id = UserLikes.objects.filter(
                    post_id=post_id_recieve, user_id=user_exist)
                like_id.delete()
                # post의 like_count 업데이트 like_count -= 1
                post_id = PostModel.objects.filter(post_id=post_id_recieve)
                count = post_id.like_count - 1
                post_id.update(like_count=count)

    else:
        return redirect('/sign-in')
    
def search(request):
    if request.method == 'POST':
        search_post = request.POST.get('search')
        print(search_post)
        result_post = PostModel.objects.all()  # 전부가져와서 search_post를 포함한 것을 출력
        find_post = [post for post in result_post if search_post in post.post_title]
        return render(request, 'contents/category.html', {'find_post': find_post})
    else:
        return render(request, 'contents/category.html')


def index_view(request):
    user = request.user.is_authenticated
    if user :
        return render(request, 'contents/index.html')
    else :
        return render(request, 'users/signin.html')
