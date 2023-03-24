from uuid import UUID

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from learn.form import VenueForm
from learn.model import Venue
from learn.view.util import pager



def venue_add(
    inbound_request: HttpRequest,
) -> HttpResponseRedirect | HttpResponse:
    is_submitted: bool = False
    if inbound_request.method == "POST":
        form: VenueForm = VenueForm(
            data=inbound_request.POST,
            files=inbound_request.FILES,
        )
        if form.is_valid():
            form.save()
            print(form.Meta.model.id)
            return HttpResponseRedirect(
                redirect_to=reverse("learn:venue_add") + "?submitted=True",
            )

    if ("submitted" in inbound_request.GET) and (
        inbound_request.GET.get("submitted") == "True"
    ):
        is_submitted = True

    form: VenueForm = VenueForm()
    return HttpResponse(
        render(
            request=inbound_request,
            template_name="learn/Venue/create.html",
            context={
                "title": "Add Venue",
                "is_submitted": is_submitted,
                "form": form,
                "user":inbound_request.user,
            },
        )
    )


def venue_list(inbound_request: HttpRequest) -> HttpResponse:
    venues = Venue.objects.all().order_by(
        "name",
        "address",
    )

    # pagination

    page = Paginator(
        Venue.objects.all().order_by(
            "name",
            "address",
        ),
        2,
    )
    current_page = inbound_request.GET.get("page")

    venues = page.get_page(current_page)

    current_page, page_list = pager(
        venues.number, venues.paginator.num_pages, 5
    )
    return HttpResponse(
        render(
            request=inbound_request,
            template_name="learn/Venue/read_all.html",
            context={
                "title": "All Venues",
                "venues": venues,
                "num_of_pages": page_list,
                "current_page": current_page,
                "user":inbound_request.user,
            },
        )
    )


def venue_read(
    inbound_request: HttpRequest,
    venue_id: UUID,
) -> HttpResponse:
    venue: Venue = Venue.objects.get(id=venue_id)
    return HttpResponse(
        render(
            request=inbound_request,
            template_name="learn/Venue/read.html",
            context={
                "title": "Venue " + venue.name,
                "venue": venue,
                "user":inbound_request.user,
            },
        )
    )



def venue_update(
    inbound_request: HttpRequest,
    venue_id: UUID,
) -> HttpResponseRedirect | HttpResponse:
    venue_instance: Venue = Venue.objects.get(id=venue_id)
    if inbound_request.method == "POST":
        form: VenueForm = VenueForm(
            data=inbound_request.POST or None,
            files=inbound_request.FILES,
            instance=venue_instance,
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                redirect_to=reverse("learn:venue_list"),
            )

    form: VenueForm = VenueForm(
        data=inbound_request.POST or None,
        instance=venue_instance,
    )
    return HttpResponse(
        render(
            request=inbound_request,
            template_name="learn/Venue/update.html",
            context={
                "title": "Update Venue",
                "form": form,
                "user":inbound_request.user,
            },
        )
    )



def venue_delete(
    inbound_request: HttpRequest,
    venue_id: UUID,
) -> HttpResponseRedirect:
    Venue.objects.get(id=venue_id).delete()
    return HttpResponseRedirect(
        redirect_to=reverse("learn:venue_list"),
    )
