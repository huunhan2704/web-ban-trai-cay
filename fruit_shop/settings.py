import os
from pathlib import Path

# Thư mục gốc của dự án
BASE_DIR = Path(__file__).resolve().parent.parent

# Bảo mật (Giữ nguyên hoặc thay đổi khi lên Production thật)
SECRET_KEY = 'django-insecure-%yw+16@@izu=h#le1i+2zt_45z+aku3+qipb8mz3pew%bcid!a'

# Bật Debug khi đang phát triển, tắt đi khi chạy chính thức
DEBUG = True

# QUAN TRỌNG: Cho phép Railway truy cập
ALLOWED_HOSTS = ['*']


# Danh sách các ứng dụng
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fruit_store', # App của bạn
    'dashboard',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # QUAN TRỌNG: Giúp hiện CSS/Ảnh trên Railway
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fruit_shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media', # Giúp dùng {{ MEDIA_URL }} trong HTML
            ],
        },
    },
]

WSGI_APPLICATION = 'fruit_shop.wsgi.application'


# Cơ sở dữ liệu (Mặc định dùng SQLite3)
##DATABASES = {
  #########}
# Cấu hình dùng PostgreSQL trên Railway
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'hnMIxCJdbLpszbQRxsDpIoOzWuHlsoaA',
        'HOST': 'postgres.railway.internal',
        'PORT': '5432',
    }
}

# Ngôn ngữ và Thời gian
LANGUAGE_CODE = 'vi-vn' # Đổi sang tiếng Việt cho thân thiện
TIME_ZONE = 'Asia/Ho_Chi_Minh'
USE_I18N = True
USE_TZ = True


# --- CẤU HÌNH FILE TĨNH (CSS, JS, LOGO) ---
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# Thêm dòng này để gom file khi chạy lệnh collectstatic trên Railway
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 


# --- CẤU HÌNH FILE MEDIA (ẢNH SẢN PHẨM, BANNER) ---
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'