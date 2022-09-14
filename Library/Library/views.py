from django.shortcuts import render

def index(request):

    template="library/index.html"
    return render(request, template)