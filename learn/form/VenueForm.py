from django import forms
from django.contrib.auth.models import User

from learn.model import Venue


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue

        fields = (
            "name",
            "address",
            "zip_code",
            "website",
            "phone",
            "email",
            "picture",
        )

        labels = {
            "name": "",
            "address": "",
            "zip_code": "",
            "website": "",
            "phone": "",
            "email": "",
            "picture": "Upload Picture",
        }
        widgets = {
            # "name": forms.widgets.TextInput(
            #     attrs={"class": "form-control", "placeholder": "Name"}
            # ),
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Name",
                }
            ),
            "address": forms.widgets.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Address",
                }
            ),
            "zip_code": forms.widgets.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Zip Code",
                }
            ),
            "website": forms.widgets.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Web Address",
                }
            ),
            "phone": forms.widgets.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Contact Number",
                }
            ),
            "email": forms.widgets.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email Address",
                }
            ),
            "picture": forms.widgets.FileInput(
                attrs={
                    "class": "form-control fw-300",
                    "required": False,
                },
            ),
        }
