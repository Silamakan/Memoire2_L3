from django.shortcuts import render

def index(request):

    template = "dashboard.html"
    return render(request, template)