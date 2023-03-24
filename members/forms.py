from typing import Any

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.widgets.EmailInput(
            attrs={
                "class": "form-control fw-300",
            },
        )
    )
    firstname = forms.CharField(
        max_length=50,
        widget=forms.widgets.TextInput(
            attrs={
                "class": "form-control fw-300",
            },
        ),
    )
    lastname = forms.CharField(
        max_length=50,
        widget=forms.widgets.TextInput(
            attrs={
                "class": "form-control fw-300",
            },
        ),
    )
    address = forms.CharField(
        max_length=200,
        widget=forms.widgets.Textarea(
            attrs={
                "class": "form-control fw-300",
                "cols": "15",
                "rows": "5",
            }
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "firstname",
            "lastname",
            "address",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control fw-300"
        self.fields["password1"].widget.attrs["class"] = "form-control fw-300"
        self.fields["password2"].widget.attrs["class"] = "form-control fw-300"
