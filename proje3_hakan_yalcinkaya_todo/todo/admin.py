from django.contrib import admin
from .models import Todo, Category


class TodoCategory(admin.ModelAdmin):
    list_display = ["title"]


class TodoAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "category",
        "title",
        "is_active",
        # "created_at",
        # "updated_at",
    ]
    list_display_links = [
        "pk",
        "category",
        "title",
    ]  # tiklanabilirlik ozelligi ekledik.


admin.site.register(Todo, TodoAdmin)
# admin icerisine Todo bilgisini aktar. (Bu models.py icerisinde olusturdugumuz tabloyu admin panelde gorebilmemizi saglar.)
# Bu satir normalde en ustteydi ama admin panel uzerindeki goruntu ayarlarini da yapacagimiz icin asagiya almak zorunda kaldik.
# Parantez icerisine ekledigimiz TodoAdmin ifadesi yukaridaki class'ta yapilan islemlerin admin panelde gorunmesini sagladi.

admin.site.register(Category)
