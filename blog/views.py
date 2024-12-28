from django.shortcuts import render

# ここにビューを作成します
def blog_home(request):
    return render(request, 'blog.html')  # blog.html テンプレートをレンダリングします