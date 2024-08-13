from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from blog_app_project.blog_app.models import BlogPost


# Create your views here.
class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-created_on"]


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blog/post_detail.html"
    context_object_name = "post"


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ["title", "body"]
    template_name = "blog/post_new.html"
    success_url = "/blog/"
    context_object_name = "post"


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ["title", "body"]
    template_name = "blog/post_new.html"
    context_object_name = "post"
    success_url = "/blog/"


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog/post_delete.html"
    context_object_name = "post"
    success_url = "/blog/"
