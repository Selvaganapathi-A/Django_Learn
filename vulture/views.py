from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import json


# Create your views here.
def index(inbound_request: HttpRequest, *args, **kwargs) -> HttpResponse:
    print(inbound_request.method)
    print(inbound_request.headers)

    print(inbound_request.COOKIES)
    if inbound_request.method == "POST":
        username = inbound_request.POST.get("username")
        password = inbound_request.POST.get("password")
        print(username, password)

    return HttpResponse(
        render(
            request=inbound_request,
            template_name="vulture/index.html",
            context={
                "hi": "google",
            },
        )
    )
