import csv
import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kizflix.settings')
django.setup()
from contents.models import PostModel

CSV_PATH_POSTS = '/Users/hanjang-won/Desktop/15zizo_project/15team_kizflix/recommend.csv'  # 경로설정 잘되었는지 확인
with open(CSV_PATH_POSTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)  # 첫 행은 출력하지 않는다.

    for row in data_reader:
        print(row[0])
        
            