from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from .Participant import Participant
from .Venue import Venue


class Event(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid4, auto_created=True, editable=False
    )
    name = models.CharField("Event Name", max_length=50)
    description = models.TextField(max_length=500, blank=True, null=True)
    event_date = models.DateTimeField("Event Date")
    event_manager = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL
    )
    venue = models.ForeignKey(
        Venue, on_delete=models.CASCADE, blank=True, null=True
    )
    participants = models.ManyToManyField(Participant, blank=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse(
            "learn:event",
            kwargs={
                "event_id": self.id,  # type:ignore
            },
        )


def main():
    User.first_name
    User.last_name


if __name__ == "__main__":
    main()
