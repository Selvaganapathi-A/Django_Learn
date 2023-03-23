from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import RegisterUserForm

# Create your views here.


def index(inbound_request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        render(
            request=inbound_request,
            template_name="authentication/index.html",
            context={
                "title": "Members",
            },
        )
    )


def register_user(inbound_request: HttpRequest) -> HttpResponse:
    if inbound_request.method == "POST":
        form = RegisterUserForm(inbound_request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(inbound_request, username=username, password=password)
            login(request=inbound_request, user=user)
            messages.success(inbound_request, ("User Registered Successfully."))
            return HttpResponseRedirect(redirect_to=reverse("learn:index"))
    form = RegisterUserForm()
    return HttpResponse(
        render(
            request=inbound_request,
            template_name="authentication/signup.html",
            context={
                "title": "Register User",
                "form": form,
            },
        )
    )

# def register_user(inbound_request: HttpRequest) -> HttpResponse:
#     if inbound_request.method == "POST":
#         form = UserCreationForm(inbound_request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data["username"]
#             password = form.cleaned_data["password1"]
#             user = authenticate(inbound_request, username=username, password=password)
#             login(request=inbound_request, user=user)
#             messages.success(inbound_request, ("User Registered Successfully."))
#             return HttpResponseRedirect(redirect_to=reverse("learn:index"))
#     form = UserCreationForm()
#     return HttpResponse(
#         render(
#             request=inbound_request,
#             template_name="authentication/signup.html",
#             context={
#                 "title": "Register User",
#                 "form": form,
#             },
#         )
#     )


def login_user(inbound_request: HttpRequest) -> HttpResponse:
    if inbound_request.method == "POST":
        username = inbound_request.POST.get("username")
        password = inbound_request.POST.get("password")
        user = authenticate(inbound_request, username=username, password=password)
        if user is not None:
            login(inbound_request, user)
            return HttpResponseRedirect(
                redirect_to=reverse("learn:index"),
            )
        else:
            messages.error(request=inbound_request, message=("login not validated.."))
            return HttpResponseRedirect(redirect_to=reverse("members:login"))

    return HttpResponse(
        render(
            request=inbound_request,
            template_name="authentication/login.html",
            context={
                "title": "Codemy - Login",
            },
        )
    )


def logout_user(inbound_request: HttpRequest) -> HttpResponse:
    logout(inbound_request)
    messages.success(request=inbound_request, message=("User logged out.."))
    return HttpResponseRedirect(redirect_to=reverse("learn:index"))
