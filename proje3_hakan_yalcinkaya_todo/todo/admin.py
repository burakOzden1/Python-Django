from django.contrib import admin
from .models import Todo



class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'is_active',
        'created_at',
        'updated_at',
    ]



admin.site.register(Todo, TodoAdmin) 
# admin icerisine Todo bilgisini aktar. (Bu models.py icerisinde olusturdugumuz tabloyu admin panelde gorebilmemizi saglar.)
# Bu satir normalde en ustteydi ama admin panel uzerindeki goruntu ayarlarini da yapacagimiz icin asagiya almak zorunda kaldik.
# Parantez icerisine ekledigimiz TodoAdmin ifadesi yukaridaki class'ta yapilan islemlerin admin panelde gorunmesini sagladi.