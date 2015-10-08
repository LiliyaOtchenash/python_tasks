from django.db import models

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):              # __unicode__ on Python 2
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter)

    def __str__(self):              # __unicode__ on Python 2
        return self.headline


r = Reporter(full_name='John Smith')
a = Article(pub_date=date.today(), headline='Django is cool',
...     content='Yeah.', reporter=r)

from django.contrib import admin

from . import models

admin.site.register(models.Article)