<!-- 

>>> from django.contrib.auth.models import User
>>> User.objects.all()
<QuerySet [<User: django@django.com>]>
>>>

-->

<!-- 

>>> from django.contrib.auth.models import User
>>> User.objects.get_or_create(username="django@django.com")
(<User: django@django.com>, False)
>>> user, created = User.objects.get_or_create(username="django@django.com")
>>> user
<User: django@django.com>
>>> created
False
>>>
# Bu kullaniciyi ya getir ya da olustur dedik, False ifadesi kullanicinin daha once kaydının oldugunu gosterir.

-->





<!-- 

>>> from blog.models import BlogPost
>>> b = BlogPost.objects.first()
>>> b.slug
'asdfasdfasdfa'
>>> b.user 
<User: django@django.com>
>>>

-->








<!-- 
>>> BlogPost.objects.first()
<BlogPost: asdfasdfasdfa>
>>> BlogPost.objects.first().pk
1
>>> post = BlogPost.objects.first() 
>>> post
<BlogPost: asdfasdfasdfa>
>>> tag1 = Tag.objects.get_or_create(title='django2)
  File "<console>", line 1
    tag1 = Tag.objects.get_or_create(title='django2)
                                           ^
SyntaxError: incomplete input
>>> tag1 = Tag.objects.get_or_create(title='django2') 
>>> tag1
(<Tag: django2>, True)
>>> tag1, created = Tag.objects.get_or_create(title='django')  
>>> tag1
<Tag: django>
>>> tag2, created = Tag.objects.get_or_create(title='django') 
>>> tag2
<Tag: django>
>>> tag2, created = Tag.objects.get_or_create(title='flask')  
>>> tag2
<Tag: flask>
>>> post.tag.add(tag1)
>>> post.tag.add(tag2) 
>>> tag3, created = Tag.objects.get_or_create(title='flutter') 
>>> post.tag.add(tag3)
>>> tag3, created = Tag.objects.get_or_create(title='vs-code') 
>>> post.tag.add(tag3)
>>>
>>>
>>> tag3.blogpost_set.all()
<QuerySet [<BlogPost: asdfasdfasdfa>, <BlogPost: python>]>
>>> tag3.blogpost_set.all()
<QuerySet [<BlogPost: asdfasdfasdfa>, <BlogPost: python>]>
>>> tag3.blogpost_set.all()
<QuerySet [<BlogPost: asdfasdfasdfa>]>
>>>
# Blogpost uzerindeki tag'lara ulasmayi denedik.
-->




<!-- 
# python komut satiri
>>> x = '[{"value":"django"},{"value":"python"},{"value":"vs-code"},{"value":"dict"},{"value":"flask"},{"value":"turbo"}]'
>>> x
'[{"value":"django"},{"value":"python"},{"value":"vs-code"},{"value":"dict"},{"value":"flask"},{"value":"turbo"}]'
>>> import json
>>> json.loads(x)
[{'value': 'django'}, {'value': 'python'}, {'value': 'vs-code'}, {'value': 'dict'}, {'value': 'flask'}, {'value': 'turbo'}]

-->









<!--

>>> from django.contrib.auth.models import User
>>> from blog.models import BlogPost            
>>> from blog.models import Tag           
>>> Tag.objects.all().update(is_active=True)
7

-->



<!--
# python manage.py shell_plus eklentisi ile yaptik.

>>> titles = [
...     'Django Form Kullanımı',
...     'Django ModelForm Yapısı',
...     'Django MVT Yapısı',
...     'Django URL Namespace',
...     'Django Template Language',
...     'Django Extentions Kullanımı',
...     'IPython',
...     'Crispy Forms Kullanımı',
...     'Easy Thumbnail Kullanımı',
...
... ]
>>>
>>> from random import randrange
>>> randrange(10, 30)
29
>>> from slugify import slugify
>>> item = BlogPost.objects.first()
>>> for title in titles:
...     item.pk = None
...     item.title = title
...     item.slug = slugify(title)
...     item.view_count = randrange(10, 100)
...     item.save()
...
>>> 
# deneme yapmak adina 9 adet daha blog post olusturduk.
-->






<!--

# python manage.py shell_plus eklentisi ile yaptik.


>>> posts = BlogPost.objects.filter(is_active=True)
>>> top_posts = posts.order_by('-view_count')[:6]
>>> top_posts
<QuerySet [<BlogPost: Django MVT Yapısı>, <BlogPost: Django ModelForm Yapısı>, <BlogPost: Django Extentions Kullanımı>, <BlogPost: django lorem>, <BlogPost: Django URL Namespace>, <BlogPost: Django Form Kullanımı>]>
>>> top_posts.count()
6
>>>

# En cok okunan postlari aldik ve siraladik.

-->