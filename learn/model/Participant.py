from uuid import uuid4

from django.db import models
from django.urls import reverse


class Participant(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid4, auto_created=True, editable=False
    )
    firstname = models.CharField("First Name", max_length=100)
    lastname = models.CharField("Last Name", max_length=100)
    phone = models.CharField("Contact Number", max_length=100)
    email = models.EmailField("Mail Address")

    class Meta:
        verbose_name = "Guest"
        verbose_name_plural = "Guests"
        ordering = ("firstname", "lastname")

    def __str__(self) -> str:
        return self.firstname + " " + self.lastname

    def get_absolute_url(self) -> str:
        return reverse(
            "learn:participant_read",
            kwargs={
                "participant_id": self.id,  # type:ignore
            },
        )
