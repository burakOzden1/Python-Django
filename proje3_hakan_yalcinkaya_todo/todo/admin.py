from django.contrib import admin
from .models import Todo

admin.site.register(Todo) 
# admin icerisine Todo bilgisini aktar. (Bu models.py icerisinde olusturdugumuz tabloyu admin panelde gorebilmemizi saglar.)