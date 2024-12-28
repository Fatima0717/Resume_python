"""
didcodingプロジェクトのASGI設定。

このファイルはASGI呼び出しをモジュールレベルの変数 ``application`` として公開します。

このファイルに関する詳細は以下を参照してください：
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'didcoding.settings')

application = get_asgi_application()
