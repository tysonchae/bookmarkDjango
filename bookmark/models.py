# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from __future__ import unicode_literals # Python 2.x 지원용

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here

@python_2_unicode_compatible
class Bookmark(models.Model):
    title = models.CharField(max_length = 100, blank=True, null=True)
    url = models.URLField('url', unique=True)

    def __str__(self):
        return self.title
