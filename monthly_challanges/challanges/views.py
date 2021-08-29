from django.http.response import (
    Http404,
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
    "december": None,
}


def months_list(request):
    page_data = {
        "months": list(challanges.keys()),
    }

    return render(request, "challanges/index.html", page_data)


def monthly_challange(request, month):

    if month not in challanges.keys():
        raise Http404("Invalid month!")

    challange = challanges.get(month.lower())

    page_data = {
        "month": month,
        "challange": challange,
    }

    return render(request, "challanges/challange.html", page_data)


def monthly_challange_by_number(request, month):
    try:
        redirect_month = list(challanges.keys())[month - 1]
        redirect_path = reverse("month-challange", args=[redirect_month])

        return HttpResponseRedirect(redirect_path)
    except IndexError:
        raise Http404("Invalid month!")
