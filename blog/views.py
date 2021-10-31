from django.contrib.auth import forms
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages.api import success
from blog.forms import CommentForm, PostCreate, UserForm, profileForm
from django.contrib.auth.forms import AuthenticationForm
from blog.models import Comments, Like, Posts
import random
# Create your views here.


def home(req):
    comments = Comments.objects.all()
    posts = Posts.objects.all()
    likes = Like.objects.all()
    user = req.user
    num = 1
    cc = {}
    lc = {}
    for i in posts:
        counter = 0
        for j in likes:
            if i.id == j.post.id:
                counter += 1
            lc[f"{i.id}"] = counter

    for i in posts:
        counter = 0
        for j in comments:
            if i.id == j.shared_post.id:
                counter += 1
            cc[f"{i.id}"] = counter
    context = {
        "posts": posts,
        "comments": comments,
        "cc": cc,
        'lc': lc,
        'user': user,'num':num
    }
    return render(req, "blog/post_list.html", context)


def register(req):
    form = UserForm()
    if req.method == "POST":
        form = UserForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password2")
            user = authenticate(username=username, password=password)
            login(req, user)
            messages.success(req, "Thanks For Registering!")
            redirect("home")
    return render(req, "blog/register.html", {"form": form})


def user_login(req):
    form = AuthenticationForm(req, data=req.POST)
    if form.is_valid():
        user = form.get_user()
        if form.is_valid():
            messages.success(req, "Login Succesful")
            login(req, user)
            return redirect("home")
    return render(req, "blog/login.html", {"form": form})


def user_logout(req):
    messages.success(req, "You Logout!")
    logout(req)
    return redirect("home")


def detail(req, id):
    post = Posts.objects.get(id=id)
    post.views = post.views + 1
    post.save()
    post_likes = post.liked.all
    is_author = False
    if post.creator.id == req.user.id:
        is_author = True
    comments = Comments.objects.filter(shared_post=post)
    comment_counter = 0
    for i in comments:
        comment_counter += 1
    if req.method == "POST":
        form = CommentForm(req.POST, user=req.user, id=post)
        if form.is_valid():
            form.save()
            messages.success(req, "Comment Shared!")
            return redirect('home')

    form = CommentForm(user=req.user, id=id)
    return render(
        req,
        "blog/post_detail.html",
        {"post": post, "form": form, "comments": comments, "cc": comment_counter,
            'post_likes': post_likes, 'is_author': is_author},
    )


def post_create(req):
    form = PostCreate(user=req.user)
    if req.method == "POST":
        form = PostCreate(req.POST, req.FILES, user=req.user)
        if form.is_valid():
            form.save()
            messages.success(req, "Blog Shared!")
            return redirect("home")
    return render(req, "blog/post_create.html", {"form": form})


def like_post(req):
    user = req.user
    if req.method == 'POST':
        post_id = req.POST.get('post_id')
        post_obj = Posts.objects.get(id=post_id)
        print(post_id, post_obj)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(
            user_id=user.id, post_id=post_id)
        if not created:
            if like.value == 'Like':
                messages.success(req, "Post Liked!")
                like.value = 'Unlike'
            else:
                like.value = 'Like'
                messages.success(req, "Post Like Removed!")
        like.save()

    return redirect('home')


def view_profile(req):
    user = req.user
    form = profileForm(instance=user)
    posts = Posts.objects.filter(creator=user.id)
    comments = Comments.objects.all()
    cc = {}
    for i in posts:
        counter = 0
        for j in comments:
            if i.id == j.shared_post.id:
                counter += 1
            cc[f"{i.id}"] = counter
    if req.method == 'POST':
        form = profileForm(req.POST, req.FILES, instance=req.user)
        if form.is_valid():
            form.save()
            messages.success(req, 'Profile Updated!')
            return redirect('home')
    return render(req, 'blog/profile.html', {'user': user, 'posts': posts, 'form': form, 'cc': cc})

def delete_post(req,id):
    Posts.objects.filter(id=id).delete()
    messages.success(req, 'Post Deleted!')
    return redirect('home')
