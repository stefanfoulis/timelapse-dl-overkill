# -*- coding: utf-8 -*-
import os


def _upload_to(filename, camera, size='original'):
    original_path = filename
    original_name = os.path.basename(original_path)
    return 'timelapse/overview/{size}/{day}/{filename}'.format(
        size=size,
        day=original_name[:10],
        filename=original_name,
    )


def original_upload_to(instance, filename):
    camera = instance.camera.name
    size = getattr(instance, 'size', 'original')
    return _upload_to(
        filename=filename,
        camera=camera,
        size=size,
    )


def thumbnail_upload_to(instance, filename):
    camera = instance.image.camera.name
    size = getattr(instance, 'size', 'original')
    return _upload_to(
        filename=filename,
        camera=camera,
        size=size,
    )
