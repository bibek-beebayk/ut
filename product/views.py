from django.shortcuts import render
from .forms import RequirementForm
from django.http import JsonResponse

# Create your views here.

def index(request):
    context = {}
    context["form"] = RequirementForm
    return render(request, "./index.html", context)


def create_requirement(request):
    if request.method=="POST":
        pass
    return JsonResponse({})