from django.shortcuts import render

def index(request):

    template = "doc/dashboard.html"
    return render(request, template)