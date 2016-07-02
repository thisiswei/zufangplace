#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys

from os.path import dirname, abspath, join
from envelop import Environment

LOCAL_FILE = lambda *path: join(abspath(dirname(__file__)), *path)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zufangplace.settings")

    # if not local, get variables from the envdir env
    try:
        items = Environment.from_folder(LOCAL_FILE('zufangplace', 'env')).items()
    except OSError:
        items = Environment.from_file(LOCAL_FILE('zufangplace', 'local.yaml')).items()

    for key, val in items:
        os.environ.setdefault(key, str(val))

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
