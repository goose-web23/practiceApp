from django.db import models
from django.db import models


class Document(models.Model):
    stage = models.ForeignKey(
        "practices.Stage",
        on_delete=models.CASCADE,
        related_name="documents",
    )
    name = models.CharField(max_length=200)
    instruction = models.TextField(blank=True)
    deadline = models.DateField(null=True, blank=True)
    filled_by = models.CharField(max_length=300, blank=True)
    signed_by = models.CharField(max_length=300, blank=True)

    template_file = models.FileField(
        upload_to="documents/templates/",
        blank=True,
    )
    example_file = models.FileField(
        upload_to="documents/examples/",
        blank=True,
    )

    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.name
