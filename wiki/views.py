from django.shortcuts import render, get_object_or_404, reverse, HttpResponse
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
    template_name = "post_list.html"
    paginate_by = 5


class PostView(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "post_view.html",
            {
                "post": post,
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "post_view.html",
            {
                "post": post,
            },
        )


class AboutUs(View):
    def get(self, request):
        return render(request, "about_us.html")


class Contact(View):
    def get(self, request):
        return render(request, "contact.html")
