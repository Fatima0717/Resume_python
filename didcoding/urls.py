from django.contrib import admin
from django.urls import path
from didcoding import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),  # Map homepage view
    path('portfolio/', views.portfolio, name='portfolio'),  # Route for the portfolio page
]
