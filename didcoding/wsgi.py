"""
didcodingプロジェクトのWSGI設定。

このファイルはWSGI呼び出しをモジュールレベルの変数 ``application`` として公開します。

このファイルに関する詳細は以下を参照してください：
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'didcoding.settings')

application = get_wsgi_application()
