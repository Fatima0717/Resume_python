from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # 管理画面
    path('admin/', admin.site.urls),

    # メインページ
    path('', views.homepage, name='home'),
    path('about/', views.about, name='about'),

    # アプリケーション
    path('portfolio/', include('portfolio.urls')),
    path('blog/', include('myblog.urls')),
]

# 開発環境での静的ファイル/メディアファイルの提供
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)