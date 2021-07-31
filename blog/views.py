# CBV 방식으로 페이지 만들기, 반복되는 기능은 이미 정의해놓은 class가 있을때가 많다. CBV를 활용해보자.
from .models import Post
from django.views.generic import ListView, DetailView


class PostList(ListView):
    model = Post
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post

# FBV 방식으로 페이지 만든 것

# from django.shortcuts import render
# from .models import Post
#
#
# # Create your views here.
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts': posts,
#         }
#     )
#
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'post': post,
#         }
#     )
