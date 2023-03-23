from calendar import HTMLCalendar
from datetime import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def calenderMonthView(
    inbound_request: HttpRequest,
    year: int = datetime.now().year,
    month: int = datetime.now().month,
) -> HttpResponse:
    htmlCalender = HTMLCalendar()
    htmlCalender.setfirstweekday(6)
    return HttpResponse(
        render(
            request=inbound_request,
            template_name="learn/calender.html",
            context={
                "title": "Codemy",
                "monthCalendar": htmlCalender.formatmonth(
                    theyear=year, themonth=month
                ),
            },
        )
    )
