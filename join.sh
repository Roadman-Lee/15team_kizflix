set 15조 프로젝트

echo Server Information.
echo --------------------------------------------

echo 프로젝트 참가 인원 : 박다희와 아이들
echo 프로젝트 기한 일자 : 2022-01-26 ~ 2022-02-09
echo 프로젝트 이름 : $1
echo PostgreSQL 버전 : 미정
echo Django 버전 : 4.0.1

echo --------------------------------------------

echo 폴더 최상위로 돌아갑니다...

echo $1 서버에 진입합니다...
python3 manage.py runserver
