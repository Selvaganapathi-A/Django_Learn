from uuid import UUID

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from learn.model import Participant


def participant_add(inbound_request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        render(
            request=inbound_request,
            template_name="",
            context={
                "title": "Event Management",
            },
        )
    )

@login_required(login_url=reverse_lazy("members:login"))
def participant_list(inbound_request: HttpRequest) -> HttpResponse:
    participants: list[Participant] = list(Participant.objects.all())
    return HttpResponse(
        render(
            request=inbound_request,
            template_name="learn/Participant/read_all.html",
            context={
                "title": "Event Management",
                "participants": participants,
            },
        )
    )

@login_required(login_url=reverse_lazy("members:login"))
def participant_read(
    inbound_request: HttpRequest, participant_id: UUID
) -> HttpResponse:
    participant: Participant = Participant.objects.get(
        Q(
            id=participant_id,
        ),
    )
    return HttpResponse(
        render(
            request=inbound_request,
            template_name="learn/Participant/read.html",
            context={
                "title": "Event Management",
                "participant": participant,
            },
        )
    )


def participant_update(
    inbound_request: HttpRequest, participant_id: UUID
) -> HttpResponse:
    return HttpResponse(
        render(
            request=inbound_request,
            template_name="",
            context={
                "title": "Event Management",
            },
        )
    )


def participant_delete(
    inbound_request: HttpRequest, participant_id: UUID
) -> HttpResponse:
    return HttpResponse(
        render(
            request=inbound_request,
            template_name="",
            context={
                "title": "Event Management",
            },
        )
    )
