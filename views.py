from django.shortcuts import render

def index(request):
    return render(request, 'myblog/index.html')  # Create this template

def myblog_detail(request, myblog_id):
    # Here you can fetch the myblog post by ID and pass it to the template
    return render(request, 'myblog/myblog-detail.html', {'myblog_id': myblog_id})  # Create this template
