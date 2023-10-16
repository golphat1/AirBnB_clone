#!/usr/bin/python3
# __init__.py

from models.engine.file_storage import FileStorage

"""creats a unique FileStorage instance for application"""
storage = FileStorage()
storage.reload()
