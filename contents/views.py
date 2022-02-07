
from django.shortcuts import render, redirect
from users.models import UserModel, UserLikes, UserProfiles
from .models import PostModel

# Create your views here.


def category_view(request):
    if request.method == 'GET':
        return render(request, 'contents/category.html')
    elif request.method == 'POST':
        user = request.user.is_authenticated
        # 1. 카테고리별 리스트 만들기
        category_list = []

        if user:
            category_post = request.POST.get('post_category', '')
            if category_post:
                post_list = PostModel.objects.filter(
                    post_category=int(category_post))
                for post in post_list:
                    category_list.append(post.post_id)

            # category.html에서 카테고리 버튼을 클릭하면 데이터를 받아온다. ex)카테고리1 = 1

            return render(request, 'contents/category.html', {'post_list': category_list})


def detail_view(request, id):
    user = request.user.is_authenticated
    if user:
        post_id_recieve = request.POST.get['post_give']
        if request.method == 'GET':
            post = PostModel.objects.get(post_id = post_id_recieve)

            return render(request, 'contets/detail.html', {'post': post})

             # recommanded_contents = UserModel.objects.get(id=id)  all에서 추천된 컨텐츠가 저장되어있는 db로 바꿔야함
            # return render(request, 'contents/detail.html', {'re_contents': recommanded_contents})

        if request.method == 'POST':

            # 정보 불러오기
            like_recieve = request.POST.get['like_give']  # 1 : 좋아요 0 : 좋아요 취소

            user_exist = UserModel.objects.get(username=request.user)

            if like_recieve == 1:
                #like에 user, post 정보 저장
                like_post = UserLikes(user_id = user_exist, post_id = post_id_recieve)
                like_post.save()

                #post의 like_count 업데이트 like_count += 1
                post_id = PostModel.objects.filter(post_id=post_id_recieve)
                count = post_id.like_count + 1
                post_id.update(like_count=count)

            else:
                #user, post정보와 일치하는 like정보 삭제
                like_id = UserLikes.objects.filter(post_id=post_id_recieve, user_id = user_exist)
                like_id.delete()
                #post의 like_count 업데이트 like_count -= 1
                post_id = PostModel.objects.filter(post_id=post_id_recieve)
                count = post_id.like_count - 1
                post_id.update(like_count=count)

    else :
        return redirect('/sign-in')

def index_view(request):

    return render(request, 'contents/index.html')
