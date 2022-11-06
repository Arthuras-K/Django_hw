from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


DATA = []

with open('1.2-requests-templates\pagination\data-398-2018-08-30.csv', encoding="utf-8") as f:
    DictReader_obj = csv.DictReader(f)
    for item in DictReader_obj:
        DATA.append({
            'Name': item['Name'], 
            'Street': item['Street'], 
            'District': item['District'],
            })

def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(DATA, 10)
    page = paginator.get_page(page_number)
    context = {
        "page": page,
        'bus_stations': page,
    }
    return render(request, 'stations/index.html', context)


