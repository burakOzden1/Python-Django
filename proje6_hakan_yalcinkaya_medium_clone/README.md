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