from django.db import models
from django.db import models


class Practice(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


class Stage(models.Model):
    practice = models.ForeignKey(
        Practice,
        on_delete=models.CASCADE,
        related_name="stages",
    )
    name = models.CharField(max_length=150)
    instructions = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    deadline = models.CharField(
        max_length=200,
        blank=True,
        default="",
        verbose_name="Срок выполнения",
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.practice.name} — {self.name}"


class Explanation(models.Model):
    stage = models.ForeignKey(
        Stage,
        on_delete=models.CASCADE,
        related_name="explanations",
        null=True,
        blank=True,
    )
    document = models.ForeignKey(
        "documents.Document",
        on_delete=models.CASCADE,
        related_name="explanations",
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=200)
    text = models.TextField()

    class Meta:
        ordering = ["id"]
        constraints = [
            models.CheckConstraint(
                condition=(
                    models.Q(stage__isnull=False, document__isnull=True)
                    | models.Q(stage__isnull=True, document__isnull=False)
                ),
                name="explanation_has_one_parent",
            ),
        ]

    def __str__(self):
        return self.title