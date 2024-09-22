from django.shortcuts import render, HttpResponse
from .models import Patient

# Create your views here.
def home(request):
    return render(request, "home.html")

def patients(request):
    items = Patient.objects.all()
    return render(request, "patients.html", {"patients": items})