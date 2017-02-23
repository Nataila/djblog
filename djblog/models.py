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

    def get_media(self):
        js = (
            '/static/plugins/kindeditor-4.1.7/kindeditor-all-min.js',
            '/static/plugins/kindeditor-4.1.7/lang/zh_CN.js',
            '/static/plugins/kindeditor-4.1.7/config.js',
        )
        media = super(PostAdmin, self).get_media()
        media.add_js(js)
        return media

xadmin.site.register(Post, PostAdmin)
