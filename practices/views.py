from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from practices.models import Explanation
from .models import Practice, Stage


def home(request):
    practices = Practice.objects.filter(active=True)

    return render(
        request,
        "practices/home.html",
        {
            "practices": practices,
        },
    )


def practice_detail(request, practice_id):
    practice = get_object_or_404(
        Practice,
        id=practice_id,
        active=True,
    )

    stages = practice.stages.all()

    return render(
        request,
        "practices/practice_detail.html",
        {
            "practice": practice,
            "stages": stages,
        },
    )


def stage_detail(request, practice_id, stage_id):
    practice = get_object_or_404(
        Practice,
        id=practice_id,
        active=True,
    )

    stage = get_object_or_404(
        Stage,
        id=stage_id,
        practice=practice,
    )

    documents = stage.documents.filter(active=True)
    explanations = Explanation.objects.filter(stage=stage)

    return render(
        request,
        "practices/stage_detail.html",
        {
            "practice": practice,
            "stage": stage,
            "documents": documents,
            "explanations": explanations,
        },
    )
