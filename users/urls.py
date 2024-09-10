from django.conf.urls.static import static
from django.urls import path, include

from .views import SignUpView, ProfileView
from django.conf import settings

app_name = "users"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", ProfileView.as_view(), name="profile")
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)