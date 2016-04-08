# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from . import models


class CameraAdmin(admin.ModelAdmin):
    pass


class DirectoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'camera',
        'image_count',
        'last_checked_at',
    )
    list_filter = (
        'camera',
    )


class ThumbnailInline(admin.TabularInline):
    model = models.Thumbnail
    extra = 0


class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'path',
        'camera',
        'shot_at',
    )
    list_filter = (
        'camera',
    )
    raw_id_fields = (
        'camera',
        'directory',
    )
    date_hierarchy = 'shot_at'
    inlines = (
        ThumbnailInline,
    )


class ThumbnailAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'size',
    )
    list_filter = (
        'size',
    )
    raw_id_fields = (
        'image',
    )

admin.site.register(models.Camera, CameraAdmin)
admin.site.register(models.Directory, DirectoryAdmin)
admin.site.register(models.Image, ImageAdmin)
admin.site.register(models.Thumbnail, ThumbnailAdmin)
