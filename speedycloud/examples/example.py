#!/usr/bin/env python
# -*- coding: utf-8 -*-

import speedycloud

BUCKET = "sdk"
CREATE_BUCKET = "new-bucket"
OBJECT = "image.png"
FILE_PATH = "./50Mb.file"

ACCESS_KEY = "YOUR-ACCESS-KEY"
SECRET_KEY = "YOUR-SECRET-KEY"

# 初始化对象存储 API Handler
oss_api = speedycloud.create_object_storage_api(ACCESS_KEY, SECRET_KEY)

# 获取 bucket 列表
print oss_api.get_services()

# 获取 object 列表
print oss_api.list(BUCKET)

# 创建 bucket
print oss_api.create_bucket(CREATE_BUCKET)

# 设置 bucket acl
print oss_api.update_bucket_acl(CREATE_BUCKET, {'x-amz-acl': "public-read"})

# 查询 bucket acl
oss_api.query_bucket_acl(CREATE_BUCKET)

# 删除 bucket
print oss_api.delete_bucket(CREATE_BUCKET)

# 大文件分段上传，封装接口
oss_api.upload_big_data(BUCKET, "50Mb.file", FILE_PATH, {'x-amz-acl': "public-read"})
