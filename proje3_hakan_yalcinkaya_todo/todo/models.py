from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title", unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "category_view",
            kwargs={
                "category_slug": self.slug,
            },
        )  # kategori bilgilerinin ekrana daha kolay sekilde getirilmesini saglar. Bu fonksiyonu navbar.html sayfasindan cagirdik


class Todo(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE) # Bunu kullanirsak Category silinirse o kategoride
    # bulunan tum todolar silinir, biz bunu istemiyoruz. Onun yerine SET_NULL yapisini kullanabiliriz. (Asagidaki gibi)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
    )  # SET_NULL dersek null=True ifadesini
    # kullanmak zorundayiz, yani null olabileceginin yetkisini vermeliyiz.

    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # her bir satir eklendiginde tarih ve saat bilgisi kaydedilsin
    updated_at = models.DateTimeField(auto_now=True)
    # Satirlar update edildiginde tarih ve saat bilgisi kaydedilsin
    # bu ikisi arasindaki fark iyi anlasilmali!!!

    def __str__(self):
        return (
            self.title
        )  # objeyi cagirdigimiz zaman varsayilan olarak title gelmesini saglar.
