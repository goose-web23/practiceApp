from django.urls import path

from . import views


urlpatterns = [
    path("", views.dashboard_home, name="dashboard_home"),

    # Практики
    path(
        "practices/",
        views.practice_list,
        name="dashboard_practice_list",
    ),
    path(
        "practices/create/",
        views.practice_create,
        name="dashboard_practice_create",
    ),
    path(
        "practices/<int:practice_id>/edit/",
        views.practice_edit,
        name="dashboard_practice_edit",
    ),
    path(
        "practices/<int:practice_id>/delete/",
        views.practice_delete,
        name="dashboard_practice_delete",
    ),

    # Этапы
    path(
        "practices/<int:practice_id>/stages/",
        views.stage_list,
        name="dashboard_stage_list",
    ),
    path(
        "practices/<int:practice_id>/stages/create/",
        views.stage_create,
        name="dashboard_stage_create",
    ),
    path(
        "practices/<int:practice_id>/stages/<int:stage_id>/edit/",
        views.stage_edit,
        name="dashboard_stage_edit",
    ),
    path(
        "practices/<int:practice_id>/stages/<int:stage_id>/delete/",
        views.stage_delete,
        name="dashboard_stage_delete",
    ),

    #doc
    path(
        "practices/<int:practice_id>/stages/<int:stage_id>/documents/",
        views.document_list,
        name="dashboard_document_list",
    ),
    path(
        "practices/<int:practice_id>/stages/<int:stage_id>/documents/create/",
        views.document_create,
        name="dashboard_document_create",
    ),
    path(
        "practices/<int:practice_id>/stages/<int:stage_id>/documents/<int:document_id>/edit/",
        views.document_edit,
        name="dashboard_document_edit",
    ),
    path(
        "practices/<int:practice_id>/stages/<int:stage_id>/documents/<int:document_id>/delete/",
        views.document_delete,
        name="dashboard_document_delete",
    ),

    path(
        "explanations/<str:parent_type>/<int:parent_id>/",
        views.explanation_list,
        name="dashboard_explanation_list",
    ),
    path(
        "explanations/<str:parent_type>/<int:parent_id>/create/",
        views.explanation_create,
        name="dashboard_explanation_create",
    ),
    path(
        "explanations/<str:parent_type>/<int:parent_id>/<int:explanation_id>/edit/",
        views.explanation_edit,
        name="dashboard_explanation_edit",
    ),
    path(
        "explanations/<str:parent_type>/<int:parent_id>/<int:explanation_id>/delete/",
        views.explanation_delete,
        name="dashboard_explanation_delete",
    ),
]