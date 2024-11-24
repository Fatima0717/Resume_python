from django.shortcuts import render

def homepage(request):
    """メインページを表示"""
    return render(request, 'index.html')

def about(request):
    """アバウトページを表示"""
    return render(request, 'about.html')