from django.shortcuts import render, get_object_or_404
from .models import Project  # Portfolio から Project に変更

def portfolio_list(request):
    """ポートフォリオ一覧を表示"""
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio_list.html', {'projects': projects})

def portfolio_detail(request, pk):
    """ポートフォリオ詳細を表示"""
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/portfolio_detail.html', {'project': project})