# 基本設定
# =========================================
from pathlib import Path
import os
from dotenv import load_dotenv

# .envファイルの読み込み
load_dotenv()

# コアの設定
# =========================================
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-=8r+5+j(4*vly*4v$t$)2%_duyd+x#^0uiz$r$7mu-49+guh3a')
DEBUG = os.getenv('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# アプリケーション設定
# =========================================
INSTALLED_APPS = [
    # Djangoデフォルトアプリ
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # サードパーティアプリケーション
    'rest_framework',
    'corsheaders',
    
    # 自作アプリケーション
    'didcoding',
    'myblog',
    'portfolio',
]

# ミドルウェア
# =========================================
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# テンプレート設定
# =========================================
ROOT_URLCONF = 'didcoding.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
        },
    },
]

# データベース設定
# =========================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'didcoding'),
        'USER': os.getenv('DB_USER', 'didcoding_user'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'your_secure_password'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# 認証設定
# =========================================
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

# 国際化設定
# =========================================
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_TZ = True

# 静的ファイル設定
# =========================================
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'static/css/optimized',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# メディアファイルの設定を追加
# =========================================
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# その他の設定
# =========================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
WSGI_APPLICATION = 'didcoding.wsgi.application'
CORS_ALLOW_ALL_ORIGINS = True

# キャッシュの設定
# =========================================
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR / 'django_cache',
        'TIMEOUT': 60 * 15,  # 15分
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

# テンプレートのキャッシュを有効化
# =========================================
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]

# セキュリティ設定の強化
# =========================================
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000  # 1年
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# CSRFの設定強化
# =========================================
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True

# コンテンツセキュリティポリシー
# =========================================
CSP_DEFAULT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")
CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'", "'unsafe-eval'")
CSP_IMG_SRC = ("'self'", "data:", "https:")

# デバッグモードがTrueの場合（開発環境）は一部のセキュリティ設定を無効化
# =========================================
if DEBUG:
    # HTTPSリダイレクトを無効化（開発環境ではHTTPを使用）
    SECURE_SSL_REDIRECT = False
    # セキュアクッキーを無効化（開発環境ではHTTPを使用）
    CSRF_COOKIE_SECURE = False
    SESSION_COOKIE_SECURE = False

# 本番環境の設定
# =========================================
if not DEBUG:
    
    # ログの設定
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'ERROR',
                'class': 'logging.FileHandler',
                'filename': BASE_DIR / 'logs/django.log',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'ERROR',
                'propagate': True,
            },
        },
    }
    
    # 静的ファイルの設定
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'