from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'loan/home.html', context)
