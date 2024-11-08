from django.apps import AppConfig

class PortfolioConfig(AppConfig):
    """ポートフォリオアプリケーションの設定"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
    verbose_name = 'ポートフォリオ'
