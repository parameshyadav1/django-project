# # Add to INSTALLED_APPS
# import os
# from pathlib import Path

# # Build paths inside the project like this: BASE_DIR / 'subdir'
# BASE_DIR = Path(__file__).resolve().parent.parent
# ROOT_URLCONF = 'backend.urls' 
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',  # Required for auth
#     'django.contrib.sessions',      # Required for admin
#     'django.contrib.messages',      # Required for admin
#     'django.contrib.staticfiles',   # Required for admin
#     'rest_framework',
#     'todo',
# ]
    

# # Add to MIDDLEWARE
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',  # Required for admin
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# # CORS settings (add at the bottom of settings.py)
# CORS_ORIGIN_ALLOW_ALL = True  # For development only
# # Or for production:
# # CORS_ORIGIN_WHITELIST = [
# #     'http://localhost:3000',
# # ]

# # REST Framework settings
# # Add to settings.py
# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.AllowAny',
#     ]
# }
# CORS_ORIGIN_ALLOW_ALL = True
# # Set DEBUG to True (temporary solution for development)
# DEBUG = True

# # OR if you want to keep DEBUG=False, set ALLOWED_HOSTS like this:
# ALLOWED_HOSTS = ['localhost', '127.0.0.1']
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'APP_DIRS': True,  # Important for admin templates
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]


# # backend/backend/settings.py
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',  # Using SQLite for simplicity
#         'NAME': BASE_DIR / 'db.sqlite3',         # Database file will be created here
#     }
# }

# # Add this to fix the auto-field warning
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# # For development
# ALLOWED_HOSTS = ['*']

# # For production (use your actual domain)
# # ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
# # Add to settings.py
# CSRF_TRUSTED_ORIGINS = [
#     'http://localhost:8000',
#     'http://127.0.0.1:8000'
# ]
import os

DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = [
        os.getenv('DOMAIN_NAME'),
        f"www.{os.getenv('DOMAIN_NAME')}",
        'localhost',
        '127.0.0.1'
    ]
    
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
# Make sure these apps are included
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'todo',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATIC_URL = '/static/'

# And these middleware classes
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Using pathlib instead of os.path
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

# Add this at the top of the file
BASE_DIR = Path(__file__).resolve().parent.parent

CORS_ORIGIN_ALLOW_ALL = True  # For development only

# Database (SQLite by default)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# backend/backend/settings.py
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'