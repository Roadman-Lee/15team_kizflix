from django.urls import path
from . import views


urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('sign-in/', views.sign_in_view, name='sign-in'),
    path('logout/', views.logout, name='logout'),
    path('mypage/<int:id>', views.like_post, name='mypage'),
    path('mypage/profile', views.profile, name='profile')
]
