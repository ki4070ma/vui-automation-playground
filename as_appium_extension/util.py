#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Any


class GlobalVar(object):

    log_root_dir = ''
    log_dir = ''

    _instance = None

    def __new__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance
