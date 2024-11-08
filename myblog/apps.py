from django.apps import AppConfig

class MyblogConfig(AppConfig):
    """ブログアプリケーションの設定"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myblog'
    verbose_name = 'ブログ'
