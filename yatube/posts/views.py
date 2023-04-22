from django.shortcuts import render,get_object_or_404
from .models import Post,Group, User
from django.core.paginator import Paginator
# Create your views here.
'''
def index(request):
    template = "posts\index.html"
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts':posts
    }
    return render(request,template,context)'''
import datetime
def index(request):
    template = "posts\index.html"
    posts_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(posts_list,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj
    }
    return render(request,template,context)

def group_posts(request,slug):
    template = "posts\group_list.html"
    group = get_object_or_404(Group,slug = slug)
    posts = Post.objects.filter(group = group).order_by('-pub_date')[:10]
    context = {
        "posts" : posts,
        "group" : group
    }
    
    return render(request,template,context)


def profile(request,username):
    template = "posts\profile.html"
    user = get_object_or_404(User,username = username)
    posts = Post.objects.filter(author = user)
    posts_count = Post.objects.filter(author = user).count
    paginator = Paginator(posts,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
            'author':user,
            'posts_count':posts_count,
            'page_obj':page_obj,
    }
    
    return render(request,template,context)


def post_detail(request,post_id):
    template = "posts\post_detail.html"
    post = get_object_or_404(Post, pk = post_id)
    posts_count = Post.objects.filter(author = post.author).count
    context = {
            'post':post,
            'posts_count':posts_count,
    }
    
    return render(request,template,context)