from django.shortcuts import render

from posts.models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})
