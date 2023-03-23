from django.urls import path

from learn.view.view_calendar import calenderMonthView
from learn.view.view_event import event_add, event_delete, event_list
from learn.view.view_event import event_read, event_update
from learn.view.view_participant import participant_add, participant_delete
from learn.view.view_participant import participant_list, participant_read
from learn.view.view_participant import participant_update
from learn.view.view_venue import venue_add, venue_delete, venue_list
from learn.view.view_venue import venue_read, venue_update
from learn.view.view_venue_exports import export_venue_csv, export_venue_pdf
from learn.view.view_venue_exports import export_venue_txt
from learn.views import index, search

app_name = "learn"

urlpatterns = [
    # Home page
    path(
        "",
        index,
        name="index",
    ),
    path(
        "search",
        search,
        name="search",
    ),
    # Venues
    path(
        "venue_add",
        venue_add,
        name="venue_add",
    ),
    path(
        "venue_list",
        venue_list,
        name="venue_list",
    ),
    path(
        "venue_read/<uuid:venue_id>",
        venue_read,
        name="venue_read",
    ),
    path(
        "venue_update/<uuid:venue_id>",
        venue_update,
        name="venue_update",
    ),
    path(
        "venue_delete/<uuid:venue_id>",
        venue_delete,
        name="venue_delete",
    ),
    # Events
    path(
        "event_add",
        event_add,
        name="event_add",
    ),
    path(
        "event_list",
        event_list,
        name="event_list",
    ),
    path(
        "event_read/<uuid:event_id>",
        event_read,
        name="event_read",
    ),
    path(
        "event_update/<uuid:event_id>",
        event_update,
        name="event_update",
    ),
    path(
        "event_delete/<uuid:event_id>",
        event_delete,
        name="event_delete",
    ),
    # Participants
    path(
        "participant_add",
        participant_add,
        name="participant_add",
    ),
    path(
        "participant_list",
        participant_list,
        name="participant_list",
    ),
    path(
        "participant_read/<uuid:participant_id>",
        participant_read,
        name="participant_read",
    ),
    path(
        "participant_update/<uuid:participant_id>",
        participant_update,
        name="participant_update",
    ),
    path(
        "participant_delete/<uuid:participant_id>",
        participant_delete,
        name="participant_delete",
    ),
    # Export Events
    path(
        "export_venues",
        export_venue_txt,
        name="export_venues",
    ),
    path(
        "export_venues_csv",
        export_venue_csv,
        name="export_venues_csv",
    ),
    path(
        "export_venues_pdf",
        export_venue_pdf,
        name="export_venues_pdf",
    ),
    # Calendar Related Views
    path(
        "calender",
        calenderMonthView,
        name="viewCalender",
    ),
    path(
        "calender/<int:year>/<int:month>",
        calenderMonthView,
        name="viewCalender",
    ),
]
