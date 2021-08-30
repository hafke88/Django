from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    profiles = ["Clint", "Seymour", "Oddjob", "Erik"]
    context = {
        'profiles': profiles,
    }
    return render(request, "home.html", context)