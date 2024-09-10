from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "blog_app"
urlpatterns = [
    path("", views.BlogPostListView.as_view(), name="index"),
    path("<int:pk>/", views.BlogPostDetailView.as_view(), name="detail"),
    path("new/", views.BlogPostCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", views.BlogPostUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", views.BlogPostDeleteView.as_view(), name="delete"),
    path("search/", views.BlogPostSearchView.as_view(), name="search")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)