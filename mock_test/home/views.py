from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegistrationForm, PostForm
from.models import Post, User
# Create your views here.
def index(request):
    Data = {'Posts': Post.objects.all().order_by("created_at")}
    return render(request, 'pages/home.html', Data)

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})


def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'pages/post.html', {'post':post})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/post')
    else:
        form = PostForm()
        return render(request, 'pages/create_post.html', {'form': form})


def delete_post(request, id):
    post = Post.objects.get(id=id).delete()
    return redirect('/post')


def update_post(request, id):
    post = Post.objects.get(pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return redirect('/post')
    else:
        form = PostForm(instance=post)
        return render(request, 'pages/update_post.html', {'form': form, 'book': post})





    

    