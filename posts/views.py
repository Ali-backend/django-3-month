from django.shortcuts import render
from django.http import HttpResponse

from posts.models import Post


def http_response(request):
    return HttpResponse("Hello World !!")


def html_response(request):
    return render(request, 'index.html')

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_detail_view(request, post_id):
    post = Post.object.get(id=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})