# **Django** Proje2:
## TODO List Projesi

### Projenin Amaçları:
* Model Yapısını Anlamak
* Django ORM Query ile Çalışmak
* MVT İlişkisini Anlamak
* Django Shell Kullanımını Anlamak
* Django Shell'de Query Kullanımı
* OneToOneField, ForeignKey ve ManyToManyField Yapılarını Anlamak
* Context Prosessor ile Genel Verileri Site içerisinde Kullanmak
* DEBUG Mode
* Settings Dosyasını Daha Fazla Tanımak

![ToDo-List Yapisi](assets/todo-list.png)

## Django ORM Query:
```shell
python manage.py shell
```

```python
# Todo Modelini import etmek:
from todo.models import Todo

# Tum Objeler:
Todo.objects.all()

# Tum objeleri say:
Todo.objects.all().count()

# Yeni Todo olusturmak:
Todo.objects.create(title="Shell Uzerinden Olusturulan Todo")
Todo.objects.create(title="Shell Uzerinden Yeni Olusturulan Todo", is_active=True)

# is_active olanlari goster
Todo.objects.filter(is_active=True)  # SELECT * FROM todo WHERE is_active=True

# is_active olanlari say:
Todo.objects.filter(is_active=True).count()

# UPDATE:
# Yapilan sorguya uyan objelerin istenilen alanlari degistirilebilir..
Todo.objects.filter(is_active=False).update(is_active=True)

# Title icinde Django gecmeyenleri bul ve Django ekle
todos = Todo.objects.exclude(title__icontains="django")

for item in todos:
    item.title = f"{item.title} - Django"
    item.save()


# id ile eleman cekme

from todo.models import Todo

Todo.objects.get(id=1)
Todo.objects.get(pk=1) # ikiside ayni sonucu verir, pk = primary key


################################################################################
>>> from todo.models import Category
>>> cats = Category.objects.all()
>>> for item in cats:
...     print(item.title, item.slug)
...
Genel genel
Django django
React react
Eğitim egitim
Python python
################################################################################
>>> from todo.models import Category
>>> Category.objects.first() # bu ifade ilk kategoriyi dondurur.                             
<Category: Genel>
>>> cat = Category.objects.first()                              
>>> cat.get_absolute_url()
'/category/genel/'
>>> 
################################################################################
>>> from todo.models import Todo
>>> tf = Todo.objects.first()
>>> tf
<Todo: merhaba ben django>
>>> tl = Todo.objects.last()
>>> tl
<Todo: merhaba ben genel>
>>> tl.tag.all()
<QuerySet [<Tag: django>, <Tag: react>, <Tag: python>, <Tag: bootstrap>, <Tag: css>, <Tag: html>]>
>>> tf.tag.all()
<QuerySet [<Tag: django>, <Tag: python>, <Tag: bootstrap>, <Tag: css>]>
>>> 
################################################################################
>>> from todo.models import Tag
>>> tag = Tag.objects.first()
>>> tag
<Tag: django>
>>> tag.todo_set.all()
<QuerySet [<Todo: merhaba ben python>, <Todo: merhaba ben genel>, <Todo: merhaba ben django>]>

```