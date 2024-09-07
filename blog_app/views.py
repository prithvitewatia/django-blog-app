import bleach
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from django.core.paginator import Paginator
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
from django.shortcuts import get_object_or_404, render


# Create your views here.
class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog_app/index.html"
    context_object_name = "posts"
    ordering = ["-updated_on"]
    paginate_by = 10


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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

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

class BlogPostSearchView(ListView):
    template_name = "blog_app/index.html"
    PAGINATION_COUNT = 10

    def get(self, request, *args, **kwargs):
        query = request.GET.get("q")
        results = []
        if query:
            # Using bleach to strip out HTML from the content before searching
            clean_content = BlogPost.objects.annotate(
                clean_content=SearchVector(bleach.clean('body', tags=[], strip=True))
            )

            # Build a search query and rank the results by relevance
            search_query = SearchQuery(query)
            results = clean_content.annotate(
                search=SearchVector('title', 'clean_content'),
                rank=SearchRank(SearchVector('title', 'clean_content'), search_query)
            ).filter(search=search_query).order_by('-rank')

        paginator = Paginator(results, self.PAGINATION_COUNT)
        page_number = request.GET.get("page")
        paginated_results = paginator.get_page(page_number)

        return render(request, self.template_name, context={
            'posts': paginated_results,
            'query': query
        })