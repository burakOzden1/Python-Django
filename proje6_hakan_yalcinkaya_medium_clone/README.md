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