#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request

def fetch(*args, **kwargs):
    # make the request
    request = urllib.request.Request(*args, **kwargs)

    # basic-ish http error handling
    try:
        with urllib.request.urlopen(request) as response:
            return response.read()

    except urllib.error.HTTPError as e:
        raise RuntimeError(f"urllib.error.HTTPError: HTTP {e.getcode()}")
