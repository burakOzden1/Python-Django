from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # bir kullanicinin bir tane profili olur
    avatar = models.ImageField(upload_to="avatar")
    instagram = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True) 
    # Sonradan admin panele bilgi ekleyebilmek icin oncelikle eklenecek bilginin parantezlerinin icerisine blank=True ifadesi eklenir,
    # makemigrations ve migrate islemleri yapilir, sonra unique=True ifadesi eklenerek tekrar makemigrations ve migrate yapilir.
