from django import forms
from django.forms import widgets

from learn.model import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            "name",
            "event_date",
            "event_manager",
            "venue",
            "participants",
            "description",
        )
        labels = {
            "name": "Event",
            "event_date": "Date of Event (YYYY-MM-DD)",
            "event_manager": "Manager",
            "venue": "Venue",
            "participants": "Attendees",
            "description": "Description",
        }

        widgets = {
            "name": widgets.TextInput(
                attrs={
                    "class": "form-control fw-300",
                    "placeholder": "Event Name",
                }
            ),
            "description": widgets.Textarea(
                attrs={
                    "class": "form-control textarea fw-300 fh-150",
                    "placeholder": "Description",
                    "resize": None,
                    "cols":40,
                    "rows":50,
                }
            ),
            "event_date": widgets.DateInput(
                attrs={
                    "class": "form-control fw-300 datetimepicker-input",
                    "type": "date",
                    "required": False,
                }
            ),
            "event_manager": forms.widgets.Select(
                attrs={
                    "class": "form-control fw-300 form-select",
                },
            ),
            "venue": forms.widgets.Select(
                attrs={
                    "class": "form-control fw-300 form-select",
                },
            ),
            "participants": forms.widgets.SelectMultiple(
                attrs={
                    "class": "form-control fw-300",
                },
            ),
        }
