from django.urls import path

from members.views import index, login_user, logout_user, register_user

app_name = "members"

urlpatterns = [
    path("", index,name="index"),
    path("register_user", register_user,name="register_user"),
    path("login", login_user,name="login"),
    path("logout", logout_user,name="logout"),
]
