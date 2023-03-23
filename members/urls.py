from django.urls import path

from members.views import login_user, logout_user, register_user

app_name = "members"

urlpatterns = [
    path("register_user", register_user,name="register_user"),
    path("login", login_user,name="login"),
    path("logout", logout_user,name="logout"),
]
