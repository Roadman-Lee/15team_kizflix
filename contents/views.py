from django.shortcuts import render, redirect
from users.models import UserModel, PostModel

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
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            recommanded_contents = UserModel.objects.get(
                id=id)  # all에서 추천된 컨텐츠가 저장되어있는 db로 바꿔야함
            return render(request, 'contents/detail.html', {'re_contents': recommanded_contents})
        else:
            return redirect('/sign-in')

def index_view(request):

    return render(request, 'contents/index.html')
