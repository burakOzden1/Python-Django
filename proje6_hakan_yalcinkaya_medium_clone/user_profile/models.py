from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from tinymce import models as tinymce_models



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # bir kullanicinin bir tane profili olur
    avatar = models.ImageField(upload_to="avatar")
    instagram = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200) 
    # Sonradan admin panele bilgi ekleyebilmek icin oncelikle eklenecek bilginin parantezlerinin icerisine blank=True ifadesi eklenir,
    # makemigrations ve migrate islemleri yapilir, sonra unique=True ifadesi eklenerek tekrar makemigrations ve migrate yapilir.
    info = tinymce_models.HTMLField(blank=True, null=True)

    def get_all_posts_url(self):
        return reverse(
            "read:all_posts_view",
            kwargs={
                "user_slug": self.slug,
            },
        )
    
    def get_profile_edit_url(self):
        return reverse("user:profile_edit_view",)
    

    
    def get_fav_url(self):
        return reverse("user:user_fav_view")