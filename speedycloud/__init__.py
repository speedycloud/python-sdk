# -*- coding: utf-8 -*-

from speedycloud.object_storage.object_storage import ObjectStorageAPI

def create_object_storage_api(access_key, secret_key):
    # 对象存储
    object_storage_api = ObjectStorageAPI(access_key, secret_key)
    return object_storage_api
