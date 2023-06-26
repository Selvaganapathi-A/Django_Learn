from uuid import UUID

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from learn.form import EventForm
from learn.model import Event


@login_required(login_url=reverse_lazy("members:login"))
def event_add(inbound_request: HttpRequest) -> HttpResponse:
    if inbound_request.method == "POST":
        form = EventForm(data=inbound_request.POST, files=inbound_request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                redirect_to=reverse(
                    "learn:event_list",
                    current_app="learn",
                )
            )
        else:
            print(form.errors)
    return HttpResponse(
        render(
            request=inbound_request,
            template_name="learn/Event/create.html",
            context={
                "title": "Add Event",
                "form": EventForm(),
                "user": inbound_request.user,
            },
        )
    )


def event_list(inbound_request: HttpRequest) -> HttpResponse:
    events: tuple[Event] = tuple(
        Event.objects.all()
        .select_related("venue", "event_manager")
        .order_by(
            "event_date",
            "name",
        )
    )
    return HttpResponse(
        render(
            request=inbound_request,
            template_name="learn/Event/read_all.html",
            context={
                "title": "Events List",
                "events": events,
                "user": inbound_request.user,
            },
        )
    )


def event_read(inbound_request: HttpRequest, event_id: UUID) -> HttpResponse:
    event: Event = Event.objects.get(
        Q(id=event_id),
    )
    return HttpResponse(
        render(
            request=inbound_request,
            template_name="learn/Event/read.html",
            context={
                "title": event.name,
                "event": event,
                "user": inbound_request.user,
            },
        )
    )


def event_update(inbound_request: HttpRequest, event_id: UUID) -> HttpResponse:
    event = Event.objects.get(
        id=event_id,
    )
    if inbound_request.method == "POST":
        form = EventForm(
            data=inbound_request.POST,
            files=inbound_request.FILES,
            instance=event,
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                redirect_to=reverse(
                    "learn:event_list",
                    current_app="learn",
                )
            )
        else:
            print(form.errors)
    form: EventForm = EventForm(instance=event)
    return HttpResponse(
        render(
            request=inbound_request,
            template_name="learn/Event/update.html",
            context={
                "title": "Update Event",
                "event": event,
                "form": form,
                "user": inbound_request.user,
            },
        )
    )


def event_delete(inbound_request: HttpRequest, event_id: UUID) -> HttpResponse:
    Event.objects.get(id=event_id).delete()
    return HttpResponseRedirect(
        redirect_to=reverse(
            "learn:event_list",
            current_app="learn",
        ),
    )
