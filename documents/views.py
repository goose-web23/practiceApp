from django.shortcuts import render

from django.shortcuts import get_object_or_404, render

from .models import Document


def document_detail(
    request,
    practice_id,
    stage_id,
    document_id,
):
    document = get_object_or_404(
        Document,
        id=document_id,
        stage_id=stage_id,
        stage__practice_id=practice_id,
        active=True,
    )

    practice = document.stage.practice
    stage = document.stage

    return render(
        request,
        "documents/document_detail.html",
        {
            "practice": practice,
            "stage": stage,
            "document": document,
        },
    )
