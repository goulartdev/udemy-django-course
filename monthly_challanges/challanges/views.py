from django.http.response import (
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.shortcuts import render
from django.urls import reverse

challanges = {
    "january": "Learn django 30 min every day",
    "february": "Go rowing 3 days a week",
    "march": "Read 10 pages every night before bed",
    "april": "Some challange for April",
    "may": "Some challange for May",
    "june": "Some challange for June",
    "july": "Some challange for July",
    "august": "Some challange for August",
    "september": "Some challange for Septmeber",
    "october": "Some challange for October",
    "november": "Some challange for November",
    "december": "Some challange for December",
}

INVALID_MONTH_RESPONSE = HttpResponseNotFound("<h1>Invalid month</h1>")


def months_list(requet):
    months_list = []

    months_list.append("<ui>")

    for month in challanges.keys():
        month_path = reverse("month-challange", args=[month])

        months_list.append("<li>")
        months_list.append(f'<a href="{month_path}">{month.capitalize()}</a>')
        months_list.append("</li>")

    months_list.append("</ui>")

    response_data = "".join(months_list)

    return HttpResponse(response_data)


def monthly_challange(request, month):
    challange = challanges.get(month.lower(), INVALID_MONTH_RESPONSE)
    response = f"<h1>{challange}</h1>"

    return HttpResponse(response)


def monthly_challange_by_number(request, month):
    try:
        redirect_month = list(challanges.keys())[month - 1]
        redirect_path = reverse("month-challange", args=[redirect_month])

        return HttpResponseRedirect(redirect_path)
    except IndexError:
        return HttpResponse(INVALID_MONTH_RESPONSE)
