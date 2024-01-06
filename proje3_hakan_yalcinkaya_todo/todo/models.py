from django.db import models
from autoslug import AutoSlugField


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title", unique=True)

    def __str__(self):
        return self.title


class Todo(models.Model):
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
