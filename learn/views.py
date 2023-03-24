from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

from learn.model import Event, Venue

# Create your views here.


def index(inbound_request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        render(
            request=inbound_request,
            template_name="learn/index.html",
            context={
                "title": "Codemy",
            },
        )
    )


@login_required(login_url="members:login")
def search(inbound_request: HttpRequest) -> HttpResponse:
    print("Hello Google....")
    if (inbound_request.method == "POST") and (
        search_query := inbound_request.POST.get("searched", False)
    ):
        venues = Venue.objects.filter(
            Q(name__contains=search_query) | Q(address__contains=search_query)
        )

        events = Event.objects.filter(
            Q(name__contains=search_query)
            | Q(description__contains=search_query)
            | Q()
        )
        print(search_query, venues, events)

        return HttpResponse(
            render(
                request=inbound_request,
                template_name="learn/search_results.html",
                context={
                    "title": "Codemy",
                    "venues": venues,
                    "events": events,
                    "no_of_results": len(venues) + len(events),
                },
            )
        )
    return HttpResponseBadRequest(
        content="Bad Request",
    )
