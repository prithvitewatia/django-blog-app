from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import BlogPostCreateUpdateForm
from .models import BlogPost
from django.shortcuts import get_object_or_404


# Create your views here.
class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog_app/index.html"
    context_object_name = "posts"
    ordering = ["-updated_on"]


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blog_app/detail.html"
    context_object_name = "post"

    def dispatch(self, request, *args, **kwargs):
        self.object = get_object_or_404(BlogPost, pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)


class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostCreateUpdateForm
    template_name = "blog_app/create_update_form.html"
    context_object_name = "post"
    success_url = reverse_lazy("blog_app:index")

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostCreateUpdateForm
    template_name = "blog_app/create_update_form.html"
    context_object_name = "post"
    success_url = reverse_lazy("blog_app:index")

    def get(self, request, *args, **kwargs):
        self.object = get_object_or_404(BlogPost, pk=kwargs["pk"])
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = get_object_or_404(BlogPost, pk=kwargs["pk"])
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    context_object_name = "post"
    success_url = reverse_lazy("blog_app:index")

    def delete(self, request, *args, **kwargs):
        self.object = get_object_or_404(BlogPost, pk=kwargs["pk"])
        self.object.delete()

        # add a message to the session for successful deletion
        messages.add_message(request, messages.SUCCESS, "Post deleted successfully!")
        return super().delete(request, *args, **kwargs)
