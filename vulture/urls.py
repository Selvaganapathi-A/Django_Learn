from django.urls import include, path

from .views import index

app_name = "vulture"
urlpatterns = [
    path("", index, name="index"),
]
