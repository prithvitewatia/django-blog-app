from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
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


class BlogPostCreateView(LoginRequiredMixin,CreateView):
    model = BlogPost
    form_class = BlogPostCreateUpdateForm
    template_name = "blog_app/create_update_form.html"
    context_object_name = "post"
    success_url = reverse_lazy("blog_app:index")

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, "Post created successfully")
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class BlogPostUpdateView(LoginRequiredMixin,UpdateView):
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
            messages.add_message(request, messages.SUCCESS, "Post updated successfully")
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class BlogPostDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = BlogPost
    context_object_name = "post"
    success_url = reverse_lazy("blog_app:index")
    success_message = "Post deleted successfully"

    def delete(self, request, *args, **kwargs):
        self.object = get_object_or_404(BlogPost, pk=kwargs["pk"])
        self.object.delete()

        return super().delete(request, *args, **kwargs)
