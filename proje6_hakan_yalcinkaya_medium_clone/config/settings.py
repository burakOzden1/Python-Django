"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-7fxt-xg7q1rwrhcf2c^7e=&8yk#r!=@7h*2i4@ki2mh+-w4v)7"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

BASE_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",  # kullaniciya mesaj vermeye yarar (sen zaten kayitlisin vb.)
    "django.contrib.staticfiles",
]


THIRD_PARTY_APPS = [
    "crispy_forms",
    "crispy_bootstrap5",
    "tinymce",
    "django_extensions",
    'easy_thumbnails',
]

MY_APPS = [
    "blog",
    "page",
    "user_profile",
    'read',
]

INSTALLED_APPS = BASE_APPS + THIRD_PARTY_APPS + MY_APPS

# CRISPY:
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"


THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (30, 30), 'crop': True},
        'avatar2x': {'size': (60, 60), 'crop': True},
        'thumbnail': {'size': (400, 300), 'crop': True},
        'page': {'size': (1000, 300), 'crop': True},
    },
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",  # mesaj gondermeye yarar.
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static_files",
]

# mediafiles ayarlari
MEDIA_URL = "media/"

MEDIA_ROOT = BASE_DIR / "media_files"
# mediafiles ayarlari

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# YAPILACAKLAR:::
# TODO: Login
# TODO: Logout
# TODO: Sign Up *Avatar? Instagram? user_slug? / one_to_one / profile
# TODO: Reset Password
# TODO: User Avatar, Instagram Account, user_slug(first_name, last_name)
# DONE: Blog App
# DONE: Post(Login Olan Kullanici)
# DONE: User Tag Olusturabilir *Kullanici tag bilgilerini virgul ile ayirarak gonderecek
# TODO: Populer olanlar/ En cok Okunanlar
# TODO: User Fav
# TODO: PAGE App Model Yapisi / Admin


# TASKS:
# TODO: proje6: Medium Clone projesinin kurulumu
# TODO: proje6: Home_view yapisi eklendi ve ayarlar guncellendi.
# TODO: proje6: settings icerisinden anasayfa ayarlarinin yapilmasi ve templates klasorunun iceriginin ayarlanmasi.
# TODO: proje6: todolarin olusturulmasi
# TODO: proje6: login.html yapisinin olusturulmasi ve login formunun eklenmesi
# TODO: proje6: login sayfalarinin bazi uyarilari verildi, devami gelecek.
# TODO: proje6: logout islemi yapildi, sayfalar olusturuldu (Bu kisim cok onemli!!!!!!)
# TODO: proje6: register formunda temel kontrollerin yapilmasi, daha da gelistirilebilir.
# TODO: proje6: register formunda gelismis kontrollerin yapilmasi, daha da gelistirilebilir.
# TODO: proje6: register işlemleri sirasinda bir hata alindi ve o giderildi.
# TODO: proje6: kullanici bilgilerinin profile modeline yazilmasi ve media files ayarlarinin yapilmasi.
# TODO: proje6: blog yazilari icin blog model yapisinin olusturulmasi.
# TODO: proje6: blog yazilari icin html yapilari olusturuldu ve bazi ayarlar yapildi.
# TODO: proje6: blog yazilarinin html sayfasindaki ve admin panel uzerindeki gorunumlerini ayarladik.
# TODO: proje6: TinyMCE Kullanımı ve PostModelForm içindeki Bilgilerin Kaydedilmesi
# TODO: proje6: blog yazilari icin form denetimlerine cesitli validatorler ekleme
# TODO: proje6: tagifyjs ile form yapisina daha guzel bir sekilde tag ekleme yapisinin eklenmesi
# TODO: proje6: tag eklerken many-to-many ile form yapisinin olusturulmasi, django extensions kurulumu ve daha bir cok onemli islem.
# TODO: proje6: formun kaydedilmesi ve messages framework kullanimi
# TODO: proje6: easy-thumbnail eklenmesi ve blog yazilarinin ana sayfa da gorulmesi 
# TODO: proje6: model yapisina ordering eklenmesi ve anasayfa duzenlemeleri
# TODO: proje6: kullaniciya tum blog postslarin gosterilmesi
# TODO: proje6: kullanici profiline get_absolute_url ile ulasilabilmesi
# TODO: proje6: post detay sayfasinin olusturulmasi ve bircok onemli islem yapildi.
# TODO: proje6: renk ayari
# TODO: proje6: url bilgilerinin duzeltilmesi ve with yapisinin template icinde kullanimi
# TODO: proje6: profil duzenleme sayfasinin form yapisi ile olusturulmasi ve daha bircok onemli islem.
# TODO: proje6: Profil Duzenleme Sayfasinin Form Duzenlemesi -Instance ve Initial Data Kullanimi
# TODO: proje6: Navbar duzenlemesi ve profil Url bilgilerinin zenginlestirilmesi
# TODO: proje6: shell kullanarak kolay sekilde post olusturma.
# TODO: proje6: shell icerisinden sorgu kullanimi. (En cok okunan postlari ekrana siraladik.)
# TODO: proje6: en cok okunan blog postlarin html sayfasinda gosterilmesi.
# TODO: proje6: Axios - Fav Yapısının Oluşturulması ve View içinde Gelen Request-Post Bilgileri. JS kodlari
# TODO: proje6: UserPostFav model yapisinin olusturulmasi ve alinan bilgilerin islenmesi.
# TODO: proje6: user profile icerisinde favorilere eklenenlerin gosterilmesi. Onemli!!!
# TODO: proje6: kullaniciya ait blogpost bilgilerinin guncellenmesi. Burasida cok onemli!!!
# TODO: proje6:
# TODO: proje6:
# TODO: proje6: