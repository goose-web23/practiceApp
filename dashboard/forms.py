from django import forms

from documents.models import Document
from practices.models import Practice, Stage
from practices.models import Explanation


class PracticeForm(forms.ModelForm):
    class Meta:
        model = Practice
        fields = [
            "name",
            "description",
            "active",
        ]

        labels = {
            "name": "Название",
            "description": "Описание",
            "active": "Активна",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Например: Производственная практика",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "rows": 5,
                }
            ),
            "active": forms.CheckboxInput(
                attrs={
                    "class": "form-checkbox",
                }
            ),
        }


class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = [
            "name",
            "instructions",
            "requirements",
            "deadline",
            "order",
        ]

        labels = {
            "name": "Название этапа",
            "instructions": "Инструкции",
            "requirements": "Требования к оформлению",
            "deadline": "Дедлайн",
            "order": "Порядок",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-input",
                }
            ),
            "instructions": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "rows": 6,
                }
            ),
            "requirements": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "rows": 6,
                }
            ),
            "deadline": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Например: до окончания практики",
                }
            ),
            "order": forms.NumberInput(
                attrs={
                    "class": "form-input",
                    "min": 0,
                }
            ),
        }


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document

        fields = [
            "name",
            "instruction",
            "deadline",
            "filled_by",
            "signed_by",
            "template_file",
            "example_file",
            "active",
            "order",
        ]

        labels = {
            "name": "Название документа",
            "instruction": "Инструкция по заполнению",
            "deadline": "Дедлайн",
            "filled_by": "Кто заполняет",
            "signed_by": "Кто подписывает",
            "template_file": "Шаблон документа",
            "example_file": "Пример заполнения",
            "active": "Активен",
            "order": "Порядок",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Например: Договор на практику",
                }
            ),
            "instruction": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "rows": 8,
                    "placeholder": (
                        "Пошаговая инструкция по заполнению документа"
                    ),
                }
            ),
            "deadline": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Например: до окончания практики",
                }
            ),
            "filled_by": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Например: студент",
                }
            ),
            "signed_by": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Например: студент и руководитель практики",
                }
            ),
            "template_file": forms.ClearableFileInput(
                attrs={
                    "class": "form-input",
                }
            ),
            "example_file": forms.ClearableFileInput(
                attrs={
                    "class": "form-input",
                }
            ),
            "active": forms.CheckboxInput(
                attrs={
                    "class": "form-checkbox",
                }
            ),
            "order": forms.NumberInput(
                attrs={
                    "class": "form-input",
                    "min": 0,
                }
            ),
        }

class ExplanationForm(forms.ModelForm):
    class Meta:
        model = Explanation
        fields = ["title", "text"]

        labels = {
            "title": "Заголовок пояснения",
            "text": "Текст пояснения",
        }

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Например, Как заполнить документ",
            }),
            "text": forms.Textarea(attrs={
                "class": "form-input",
                "rows": 6,
                "placeholder": "Введите пояснение...",
            }),
        }