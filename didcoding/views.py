from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def portfolio(request):
    return render(request, 'portfolio.html')