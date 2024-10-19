from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('didcoding.urls')),  # Main site urls
    path('blog', include('blog.urls')),  # Include blog's urls
    path('myblog', include('myblog.urls')),  # Include myblog's urls
]
