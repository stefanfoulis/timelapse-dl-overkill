# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import os
import exifread
import dateutil.parser
import datetime


def check_stick_connected(path):
    # checks whether the .itsmounted file exists in the path
    filepath = os.path.join(path, '.itsmounted')
    return os.path.exists(filepath)


def makedirs(path):
    try:
        os.makedirs(target_dir)
    except:
        pass


def upload_to_thumbnail(instance, filename, size=None):
    original_path = instance.original.name
    original_name = os.path.basename(original_path)
    return 'timelapse/overview/{size}/{day}/{filename}'.format(
        size=size,
        day=original_name[:10],
        filename=original_name,
    )


def extract_exif_date(image_path):
    with open(image_path, 'rb') as img_file:
        tags = exifread.process_file(img_file)
    datetime_str = str(tags['EXIF DateTimeOriginal'])
    datetime_native = datetime.datetime.strptime(datetime_str + 'UTC', '%Y:%m:%d %H:%M:%S%Z')
    return datetime_native
