from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import LogIn_Form

# Create your views here.
def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())
def login_page(request):
    template = loader.get_template("./login_page.html", {"form": form})
    return HttpResponse(template.render())
def login(request):
    form = LogIn_Form()
    template = loader.get_template("./login_page.html", {"form": form})
    return HttpResponse(template.render())
