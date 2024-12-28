"""
Django設定ファイル for didcodingプロジェクト。

このファイルはDjango 5.1.1で 'django-admin startproject' を使用して生成されました。

このファイルに関する詳細は以下を参照してください：
https://docs.djangoproject.com/en/5.1/topics/settings/

設定項目とその値の全リストについては以下を参照してください：
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# プロジェクト内のパスを以下のように構築します: BASE_DIR / 'サブディレクトリ'
BASE_DIR = Path(__file__).resolve().parent.parent


# 開発用の簡易設定 - 本番環境には不適切
# 詳細は以下を参照してください：
# https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# セキュリティ警告: 本番環境では使用する秘密鍵を必ず隠してください！
SECRET_KEY = 'django-insecure-=8r+5+j(4*vly*4v$t$)2%_duyd+x#^0uiz$r$7mu-49+guh3a'

# セキュリティ警告: 本番環境ではDEBUGを有効にしないでください！
DEBUG = True

ALLOWED_HOSTS = []


# アプリケーションの定義

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'didcoding', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'didcoding.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'didcoding.wsgi.application'


# データベース
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# パスワード検証
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# 国際化
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# 静的ファイル (CSS、JavaScript、画像など)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR / 'static']

STATIC_ROOT = BASE_DIR / 'staticfiles'

# デフォルトのプライマリキーのフィールドタイプ
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
