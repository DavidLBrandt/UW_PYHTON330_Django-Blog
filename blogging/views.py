from django.shortcuts import render, redirect
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from blogging.forms import MyPostForm
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PostListView(ListView):
    queryset = Post.objects.filter(published_date__isnull=False).order_by(
        "-published_date"
    )
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    queryset = Post.objects.filter(published_date__isnull=False)
    template_name = "blogging/detail.html"


def add_model(request):

    if request.method == "POST":
        form = MyPostForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.published_date = timezone.now()
            model_instance.author = User.objects.get(username='Anonymous')
            model_instance.save()
            return redirect('/')

    else:

        form = MyPostForm()

        return render(request, "add.html", {'form': form})
