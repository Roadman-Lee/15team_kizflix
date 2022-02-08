from django.urls import path
from . import views

urlpatterns = [
    path('category/<slug:slug>', views.category_view, name='category'),
    path('detail/<int:post_id>', views.detail_view, name='detail'),
    path('search/', views.search, name='search'),
    path('', views.index_view, name='index'),
]
