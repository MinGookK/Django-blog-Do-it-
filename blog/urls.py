from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    # path('<int:pk>/', views.single_post_page),
    # path('', views.index),  FBV 방식에서 사용하던 함수
]
