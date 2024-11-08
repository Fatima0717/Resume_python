from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_list(request):
    """ブログ記事一覧を表示"""
    blogs = Blog.objects.all()
    return render(request, 'myblog/blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    """ブログ記事の詳細を表示"""
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'myblog/blog_detail.html', {'blog': blog})