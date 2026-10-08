from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path(
        "practice/<int:practice_id>/",
        views.practice_detail,
        name="practice_detail",
    ),
    path(
        "practice/<int:practice_id>/stage/<int:stage_id>/",
        views.stage_detail,
        name="stage_detail",
    ),
]