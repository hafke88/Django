from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    profiles = []
    context = {
        'profiles': profiles,
    }
    return render(request, "home.html", context)