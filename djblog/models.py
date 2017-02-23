#!/usr/bin/env python
# coding: utf-8
# cc @ 2017-02-23

import xadmin
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'文章标题')
    content = models.TextField(verbose_name=u'文章内容')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')


class PostAdmin(object):
    list_display = ('title', 'created_at',)

xadmin.site.register(Post, PostAdmin)
