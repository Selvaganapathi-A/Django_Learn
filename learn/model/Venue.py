from uuid import uuid4

from django.db import models
from django.urls import reverse


class Venue(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid4, auto_created=True, editable=False
    )
    name = models.CharField("Venue Name", max_length=50)
    address = models.CharField(max_length=200)
    zip_code = models.CharField("Zip Code", max_length=50)
    website = models.URLField("Website Address", unique=True)
    phone = models.CharField("Contact Number", max_length=20)
    email = models.EmailField("Contact EmailID")
    picture = models.ImageField(
        "Venue Picture", upload_to="venue", default=None, null=True, blank=True
    )

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse(
            "learn:venue_read",
            kwargs={
                "venue_id": self.id,
            },
        )
