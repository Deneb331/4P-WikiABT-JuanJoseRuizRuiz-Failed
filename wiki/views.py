from django.shortcuts import render
from django.views import generic, View
from .models import Category, Post


class CategoryList(generic.ListView):
    model = Category
    queryset = Category.objects.all().order_by("title")
    template_name = "index.html"
    paginate_by = 5


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("title")
    template_name = "category_view.html"
    paginate_by = 5
