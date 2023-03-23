import csv
import io

from django.http import FileResponse, HttpRequest, HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

from learn.model import Venue


def export_venue_txt(
    inbound_request: HttpRequest,
) -> HttpResponse:
    response: HttpResponse = HttpResponse(
        content_type="text/plain",
    )
    response["Content-Disposition"] = 'attachment; filename="venues.txt"'

    lines: list[str] = []

    venues = Venue.objects.all().order_by("picture", "email")

    for venue in venues:
        venue: Venue
        lines.append(venue.name + "\n")
        lines.append(venue.address + "\n")
        lines.append(venue.zip_code + "\n")
        lines.append(venue.website + "\n")
        lines.append(venue.phone + "\n\n")

    response.writelines(lines=lines)

    return response


def export_venue_csv(
    inbound_request: HttpRequest,
) -> HttpResponse:
    # Create response
    response: HttpResponse = HttpResponse(
        content_type="text/csv",
    )
    response["Content-Disposition"] = 'attachment; filename="venues.csv"'

    # Create Csv Writer
    writer = csv.writer(response)

    writer.writerow(
        ["Name", "Address", "Zip Code", "phone", "website", "email"]
    )

    # Get Venues from database
    venues = Venue.objects.all().order_by("picture", "email")

    for venue in venues:
        venue: Venue

        writer.writerow(
            [
                venue.name,
                venue.address,
                venue.zip_code,
                venue.phone,
                venue.website,
                venue.email,
            ]
        )

    return response


def export_venue_pdf(
    inbound_request: HttpRequest,
) -> FileResponse:
    # create Filestream Buffer
    buffer = io.BytesIO()
    # create Canvas
    c = canvas.Canvas(buffer, pagesize=A4, bottomup=0)  # type: ignore

    # Create text obj
    textobj = c.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont("Helvetica", 10)

    # Get data from database
    venues = Venue.objects.all().order_by("picture", "email")

    # Loop through data
    for venue in venues:
        venue: Venue
        textobj.textLine
        textobj.textLine(venue.name)
        textobj.textLine(venue.address)
        textobj.textLine(venue.zip_code)
        textobj.textLine(venue.website)
        textobj.textLine(venue.phone)
        textobj.textLine("")
        textobj.textLine("")

    # Finish up
    c.drawText(textobj)
    c.showPage()
    c.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="venues.pdf")
