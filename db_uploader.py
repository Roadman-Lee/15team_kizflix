
import csv
import os
import django

# python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kizflix.settings')

# python파일에서 django를 실행
django.setup()

# CSV_PATH_POSTS에 csv파일 저장
# 경로설정 잘되었는지 확인
CSV_PATH_POSTS = '/Users/hanjang-won/Desktop/15zizo_project_final/15team_kizflix/animation.csv'
from contents.models import PostModel


# csv파일을 DB에 저장하는 함수
def insert_post():
    with open(CSV_PATH_POSTS) as in_file:
        data_reader = csv.reader(in_file) # csv 읽기
        next(data_reader, None)  # 첫 행은 출력하지 않는다.

        for row in data_reader:
            if not PostModel.objects.filter(post_url=row[1]).exists():  # 중복값제거
                new_post_thumbnail = row[0]
                new_post_url = row[1]
                new_post_title = row[2]

                PostModel.objects.create(
                    post_thumbnail=new_post_thumbnail,
                    post_url=new_post_url,
                    post_title=new_post_title,
                    post_category='animation',
                )


insert_post()


# def insert_recommend():
#     with open(CSV_PATH_POSTS,encoding='cp949') as in_file:
#         data_reader = csv.reader(in_file)
#         next(data_reader, None)

#         for row in data_reader:
#             if row:
#                 if not RecommendModel.objects.filter(re_title=row[0]).exists():
#                     new_re_title = row[0]
#                 RecommendModel.objects.create(re_title=new_re_title)

# insert_recommend()
