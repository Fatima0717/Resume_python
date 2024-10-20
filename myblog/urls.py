from django.urls import path
from . import views

urlpatterns = [
    path('myblog/', views.myblog_home, name='myblog_home'),  # example path for myblog
]
