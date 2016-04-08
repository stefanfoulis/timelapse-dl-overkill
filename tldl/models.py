# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import uuid

from django.db import models
from yurl import URL


class UUIDAuditedModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    _created_at = models.DateTimeField(auto_now_add=True)
    _updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Camera(UUIDAuditedModel):
    name = models.CharField(blank=True, default='', max_length=255, unique=True)
    url = models.CharField(blank=True, default='http://10.5.5.9', max_length=255)

    def __str__(self):
        return self.name

    def delete_image(self, imgpath):
        rel_path = url.split('/DCIM')[-1]
        # log('deleting {}'.format(rel_path))
        requests.get(
            "{}/gp/gpControl/command/storage/delete?p={}".format(
                self.url,
                rel_path,
            ),
        )

    def discover_directories(self):
        pass


class Directory(UUIDAuditedModel):
    camera = models.ForeignKey(Camera, related_name='directories')
    name = models.CharField(max_length=255)
    discovered_at = models.DateTimeField(null=True, blank=True, default=None)
    last_checked_at = models.DateTimeField(null=True, blank=True, default=None)
    image_count = models.IntegerField(blank=True, default=None)


class Image(UUIDAuditedModel):
    camera = models.ForeignKey(Camera, related_name='images')
    directory = models.ForeignKey(Directory, related_name='images', null=True, blank=True)
    path = models.CharField(max_length=255)
    discovered_at = models.DateTimeField(null=True, blank=True, default=None)
    downloaded_at = models.DateTimeField(null=True, blank=True, default=None)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)
    uploaded_at = models.DateTimeField(null=True, blank=True, default=None)
    file = models.FileField(blank=True, default='', max_length=255)
    shot_at = models.DateTimeField(null=True, blank=True, default=None)
    url = models.CharField(blank=True, default='', max_length=255)

    class Meta:
        unique_together = (
            'camera',
            'path',
        )


class Thumbnail(UUIDAuditedModel):
    SIZE_CHOICES = ('640x480', '320x240', '160x120')
    image = models.ForeignKey(Image, related_name='thumbnails')
    size = models.CharField(choices=zip(SIZE_CHOICES, SIZE_CHOICES), max_length=32)
    generated_at = models.DateTimeField(null=True, blank=True, default=None)
    uploaded_at = models.DateTimeField(null=True, blank=True, default=None)
    file = models.FileField(blank=True, default='', max_length=255)
    url = models.CharField(blank=True, default='', max_length=255)

    class Meta:
        unique_together = (
            'image',
            'size',
        )
