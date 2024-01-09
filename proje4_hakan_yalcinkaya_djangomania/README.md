```
###########################################################
>>> from blog.models import Post
>>> Post.objects.create(user_id=1, category_id=1, title="Django Shell", content="Fusce maximus ligula eget imperdiet sodales. Phasellus eget porta nisi. Integer vitae dolor vitae odio maximus consectetur. In nec malesuada nulla. Nullam luctus, sem ac sagittis pharetra, nunc nibh commodo leo, sed pellentesque nulla ligula nec diam. Mauris velit enim, luctus ornare vestibulum non, imperdiet non enim. Sed pellentesque elit at arcu feugiat, et laoreet tortor tincidunt. Nunc suscipit velit sit amet ex faucibus, quis suscipit libero fermentum. Pellentesque vel commodo risus. Nullam eu hendrerit est. Ut ex lacus, euismod et viverra eu, faucibus nec odio. Nam convallis risus sit amet ex fermentum, id finibus lacus efficitur. Nulla lobortis, ligula quis sodales interdum, turpis nulla interdum dolor, vitae consectetur diam tellus sed lectus. Sed ultrices sapien ipsum, eu rhoncus ligula finibus gravida. Nunc porttitor fermentum justo vitae venenatis. Nulla ac justo laoreet, pretium erat vitae, elementum dolor.", is_active=True)
<Post: Django Shell>
>>> 

###########################################################
>>> Post.objects.exclude(id__in=[1, 2]).count()                                                                                                                                                                                
4   
# birinci ve ikinci deger disindakilerin sayisini verir.
###########################################################
>>> Post.objects.exclude(id__in=[1, 2]).delete()                                                                                                                                                                               
(4, {'blog.Post': 4})  
# birinci ve ikinci deger disindakilerin hepsini siler.
###########################################################
items = Post.objects.all()
for id in range(21):
    if not id % 2 == 0:
        obj = items[0]
    else:
        obj = items[1]
    obj.pk = None
    obj.title = f"{obj.title} - {id}"
    obj.save()
# database icerisine shell uzerinden daha hizli sekilde veri ekledik.
###########################################################

>>> from slugify import slugify
>>> from blog.models import Post
>>> items = Post.objects.all()
>>> for item in items:   
...     item.slug = f"{slugify(item.title)}-{item.pk}"
...     item.save()
...
>>> for item in items:
...     print(item.slug)
...
django-bilgileri-1
django-shell-2
django-shell-0-7
django-bilgileri-1-8
django-shell-2-9
django-bilgileri-3-10
django-shell-4-11
django-bilgileri-5-12
django-shell-6-13
django-bilgileri-7-14
django-shell-8-15
django-bilgileri-9-16
django-shell-10-17
django-bilgileri-11-18
django-shell-12-19
django-bilgileri-13-20
django-shell-14-21
django-bilgileri-15-22
django-shell-16-23
django-bilgileri-17-24
django-shell-18-25
django-bilgileri-19-26
django-shell-20-27

# her bir post icin slug olusturduk
>>> slugify(items[0].title)
'django-bilgileri'
# 0'inci item'in title'inin slug bilgisini aldik.
###########################################################
>>> Post.objects.last().pk
28
>>> Post.objects.last().title
'merhaba Python öğçocamoce çğqcüöocn'
>>> Post.objects.last().slug 
'merhaba-python-ogcocamoce-cgqcuoocn'
# son ekledigimiz postun pk'sini, title'ını ve olusturulan slug bilgisini getirdik.
###########################################################
>>> from blog.models import BlogTag, Post
>>> BlogTag.objects.first()
<BlogTag: auth>
>>> tag = BlogTag.objects.first() 
>>> Post.objects.filter(tag=tag) 
<QuerySet [<Post: Django deneme - 2>, <Post: Django deneme - 3>]>
# tag bilgisinin gelip gelmemesinin kontrolu

>>> Post.objects.filter(tag=tag).first()
<Post: Django deneme - 2>
>>> i = Post.objects.filter(tag=tag).first() 
>>> i.tag.all()
<QuerySet [<BlogTag: auth>, <BlogTag: forms>, <BlogTag: models>, <BlogTag: urls>]>
# tek bir blog postun icerdigi tag bilgilerini getirmek icin kullandik.
###########################################################
###########################################################
###########################################################
###########################################################
```
```