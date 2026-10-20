from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404

from practices.models import Practice, Stage
from .forms import DocumentForm, PracticeForm, StageForm

from practices.models import Explanation
from documents.models import Document
from .forms import ExplanationForm

def staff_required(view_func):
    return user_passes_test(
        lambda user: user.is_authenticated and user.is_staff,
        login_url="login",
    )(view_func)


@staff_required
def dashboard_home(request):
    practices = Practice.objects.all().prefetch_related("stages")

    return render(
        request,
        "dashboard/home.html",
        {
            "practices": practices,
        },
    )


@staff_required
def practice_list(request):
    practices = Practice.objects.all()

    return render(
        request,
        "dashboard/practices/list.html",
        {
            "practices": practices,
        },
    )


@staff_required
def practice_create(request):
    if request.method == "POST":
        form = PracticeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("dashboard_practice_list")
    else:
        form = PracticeForm()

    return render(
        request,
        "dashboard/practices/form.html",
        {
            "form": form,
            "title": "Добавить практику",
            "submit_text": "Создать практику",
        },
    )


@staff_required
def practice_edit(request, practice_id):
    practice = get_object_or_404(Practice, id=practice_id)

    if request.method == "POST":
        form = PracticeForm(request.POST, instance=practice)

        if form.is_valid():
            form.save()
            return redirect("dashboard_practice_list")
    else:
        form = PracticeForm(instance=practice)

    return render(
        request,
        "dashboard/practices/form.html",
        {
            "form": form,
            "practice": practice,
            "title": "Редактировать практику",
            "submit_text": "Сохранить изменения",
        },
    )


@staff_required
def practice_delete(request, practice_id):
    practice = get_object_or_404(Practice, id=practice_id)

    if request.method == "POST":
        practice.delete()
        return redirect("dashboard_practice_list")

    return render(
        request,
        "dashboard/practices/delete.html",
        {
            "practice": practice,
        },
    )

@staff_required
def stage_list(request, practice_id):
    practice = get_object_or_404(
        Practice,
        id=practice_id,
    )

    stages = practice.stages.all()

    return render(
        request,
        "dashboard/stages/list.html",
        {
            "practice": practice,
            "stages": stages,
        },
    )


@staff_required
def stage_create(request, practice_id):
    practice = get_object_or_404(
        Practice,
        id=practice_id,
    )

    if request.method == "POST":
        form = StageForm(request.POST)

        if form.is_valid():
            stage = form.save(commit=False)
            stage.practice = practice
            stage.save()

            return redirect(
                "dashboard_stage_list",
                practice_id=practice.id,
            )
    else:
        form = StageForm()

    return render(
        request,
        "dashboard/stages/form.html",
        {
            "practice": practice,
            "form": form,
            "title": "Добавить этап",
            "submit_text": "Создать этап",
        },
    )


@staff_required
def stage_edit(request, practice_id, stage_id):
    practice = get_object_or_404(
        Practice,
        id=practice_id,
    )

    stage = get_object_or_404(
        Stage,
        id=stage_id,
        practice=practice,
    )

    if request.method == "POST":
        form = StageForm(
            request.POST,
            instance=stage,
        )

        if form.is_valid():
            form.save()

            return redirect(
                "dashboard_stage_list",
                practice_id=practice.id,
            )
    else:
        form = StageForm(instance=stage)

    return render(
        request,
        "dashboard/stages/form.html",
        {
            "practice": practice,
            "stage": stage,
            "form": form,
            "title": "Редактировать этап",
            "submit_text": "Сохранить изменения",
        },
    )


@staff_required
def stage_delete(request, practice_id, stage_id):
    practice = get_object_or_404(
        Practice,
        id=practice_id,
    )

    stage = get_object_or_404(
        Stage,
        id=stage_id,
        practice=practice,
    )

    if request.method == "POST":
        stage.delete()

        return redirect(
            "dashboard_stage_list",
            practice_id=practice.id,
        )

    return render(
        request,
        "dashboard/stages/delete.html",
        {
            "practice": practice,
            "stage": stage,
        },
    )

@staff_required
def document_list(request, practice_id, stage_id):
    practice = get_object_or_404(
        Practice,
        id=practice_id,
    )

    stage = get_object_or_404(
        Stage,
        id=stage_id,
        practice=practice,
    )

    documents = stage.documents.all()

    return render(
        request,
        "dashboard/documents/list.html",
        {
            "practice": practice,
            "stage": stage,
            "documents": documents,
        },
    )


@staff_required
def document_create(request, practice_id, stage_id):
    practice = get_object_or_404(
        Practice,
        id=practice_id,
    )

    stage = get_object_or_404(
        Stage,
        id=stage_id,
        practice=practice,
    )

    if request.method == "POST":
        form = DocumentForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            document = form.save(commit=False)
            document.stage = stage
            document.save()

            return redirect(
                "dashboard_document_list",
                practice_id=practice.id,
                stage_id=stage.id,
            )
    else:
        form = DocumentForm()

    return render(
        request,
        "dashboard/documents/form.html",
        {
            "practice": practice,
            "stage": stage,
            "form": form,
            "title": "Добавить документ",
            "submit_text": "Создать документ",
        },
    )


@staff_required
def document_edit(
    request,
    practice_id,
    stage_id,
    document_id,
):
    practice = get_object_or_404(
        Practice,
        id=practice_id,
    )

    stage = get_object_or_404(
        Stage,
        id=stage_id,
        practice=practice,
    )

    document = get_object_or_404(
        Document,
        id=document_id,
        stage=stage,
    )

    if request.method == "POST":
        form = DocumentForm(
            request.POST,
            request.FILES,
            instance=document,
        )

        if form.is_valid():
            form.save()

            return redirect(
                "dashboard_document_list",
                practice_id=practice.id,
                stage_id=stage.id,
            )
    else:
        form = DocumentForm(instance=document)

    return render(
        request,
        "dashboard/documents/form.html",
        {
            "practice": practice,
            "stage": stage,
            "document": document,
            "form": form,
            "title": "Редактировать документ",
            "submit_text": "Сохранить изменения",
        },
    )


@staff_required
def document_delete(
    request,
    practice_id,
    stage_id,
    document_id,
):
    practice = get_object_or_404(
        Practice,
        id=practice_id,
    )

    stage = get_object_or_404(
        Stage,
        id=stage_id,
        practice=practice,
    )

    document = get_object_or_404(
        Document,
        id=document_id,
        stage=stage,
    )

    if request.method == "POST":
        document.delete()

        return redirect(
            "dashboard_document_list",
            practice_id=practice.id,
            stage_id=stage.id,
        )

    return render(
        request,
        "dashboard/documents/delete.html",
        {
            "practice": practice,
            "stage": stage,
            "document": document,
        },
    )

@staff_required
def explanation_list(request, parent_type, parent_id):
    if parent_type == "stage":
        parent = get_object_or_404(Stage, id=parent_id)
        explanations = Explanation.objects.filter(stage=parent)
        parent_name = parent.name

    elif parent_type == "document":
        parent = get_object_or_404(Document, id=parent_id)
        explanations = Explanation.objects.filter(document=parent)
        parent_name = parent.name

    else:
        raise Http404("Неизвестный тип объекта")

    return render(
        request,
        "dashboard/explanations/list.html",
        {
            "explanations": explanations,
            "parent": parent,
            "parent_type": parent_type,
            "parent_name": parent_name,
        },
    )


@staff_required
def explanation_create(request, parent_type, parent_id):
    if parent_type == "stage":
        parent = get_object_or_404(Stage, id=parent_id)
        parent_name = parent.name

    elif parent_type == "document":
        parent = get_object_or_404(Document, id=parent_id)
        parent_name = parent.name

    else:
        raise Http404("Неизвестный тип объекта")

    if request.method == "POST":
        form = ExplanationForm(request.POST)

        if form.is_valid():
            explanation = form.save(commit=False)

            if parent_type == "stage":
                explanation.stage = parent
                explanation.document = None
            else:
                explanation.document = parent
                explanation.stage = None

            explanation.save()

            return redirect(
                "dashboard_explanation_list",
                parent_type=parent_type,
                parent_id=parent.id,
            )
    else:
        form = ExplanationForm()

    return render(
        request,
        "dashboard/explanations/form.html",
        {
            "form": form,
            "parent": parent,
            "parent_type": parent_type,
            "parent_name": parent_name,
            "page_title": "Добавить пояснение",
        },
    )


@staff_required
def explanation_edit(
    request,
    parent_type,
    parent_id,
    explanation_id,
):
    if parent_type == "stage":
        parent = get_object_or_404(Stage, id=parent_id)
        explanation = get_object_or_404(
            Explanation,
            id=explanation_id,
            stage=parent,
        )

    elif parent_type == "document":
        parent = get_object_or_404(Document, id=parent_id)
        explanation = get_object_or_404(
            Explanation,
            id=explanation_id,
            document=parent,
        )

    else:
        raise Http404("Неизвестный тип объекта")

    if request.method == "POST":
        form = ExplanationForm(
            request.POST,
            instance=explanation,
        )

        if form.is_valid():
            form.save()

            return redirect(
                "dashboard_explanation_list",
                parent_type=parent_type,
                parent_id=parent.id,
            )
    else:
        form = ExplanationForm(instance=explanation)

    return render(
        request,
        "dashboard/explanations/form.html",
        {
            "form": form,
            "parent": parent,
            "parent_type": parent_type,
            "parent_name": parent.name,
            "page_title": "Редактировать пояснение",
        },
    )


@staff_required
def explanation_delete(
    request,
    parent_type,
    parent_id,
    explanation_id,
):
    if parent_type == "stage":
        parent = get_object_or_404(Stage, id=parent_id)
        explanation = get_object_or_404(
            Explanation,
            id=explanation_id,
            stage=parent,
        )

    elif parent_type == "document":
        parent = get_object_or_404(Document, id=parent_id)
        explanation = get_object_or_404(
            Explanation,
            id=explanation_id,
            document=parent,
        )

    else:
        raise Http404("Неизвестный тип объекта")

    if request.method == "POST":
        explanation.delete()

        return redirect(
            "dashboard_explanation_list",
            parent_type=parent_type,
            parent_id=parent.id,
        )

    return render(
        request,
        "dashboard/explanations/delete.html",
        {
            "explanation": explanation,
            "parent": parent,
            "parent_type": parent_type,
        },
    )