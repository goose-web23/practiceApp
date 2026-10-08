from django.urls import path

from . import views


urlpatterns = [
    path(
        "practice/<int:practice_id>/stage/<int:stage_id>/document/<int:document_id>/",
        views.document_detail,
        name="document_detail",
    ),
]