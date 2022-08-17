from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.

def homepage(request: HttpRequest) -> HttpResponse:
    return render(request, "homepage.html")
