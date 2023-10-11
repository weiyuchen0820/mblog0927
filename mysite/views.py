from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    posts = Post.objects.all() #select from post
    post_lists = list()
    for counter,post in enumerate(posts):
        post_lists.append(f'No. {counter} {post} <br>')
    return HttpResponse(post_lists)