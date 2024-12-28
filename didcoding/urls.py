from django.contrib import admin
from django.urls import path
from didcoding import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),  # マップのホームページ用ルート
    path('portfolio/', views.portfolio, name='portfolio'),  # ルート用のポートフォリオ
    path('contact/', views.contact, name='contact'), #ルート用のコンタクト
    path('blog/', views.blog, name='blog'), # ブログのホームページ用ルート
     
]
