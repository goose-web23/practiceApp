from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path


urlpatterns = [
    path("", include("practices.urls")),
    path("accounts/", include("accounts.urls")),
    path("documents/", include("documents.urls")),
    path("admin/", include("dashboard.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )