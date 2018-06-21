# SpeedyCloud ObjectStore SDK for Python

## 依赖

```bash
lxml
```

## 安装

```bash
# git clone https://github.com/speedycloud/python-sdk.git
# cd python-sdk
# python setup.py install 
```
## 运行环境

SDK 版本 |  Python 版本
---|---
1.x | 2.6, 2.7

## 使用方法

## 获取桶列表

```python
import speedycloud

BUCKET = "bucket"

ACCESS_KEY = "YOUR-ACCESS-KEY"
SECRET_KEY = "YOUR-SECRET-KEY"

# 初始化对象存储 API Handler
oss_api = speedycloud.create_object_storage_api(ACCESS_KEY, SECRET_KEY)

# 获取 bucket 列表
print oss_api.list(BUCKET)
```

### 上传大文件

示例：采用分段上传大文件，并设置公共读权限

```python
import speedycloud

BUCKET = "bucket"
OBJECT = "object"
FILE_PATH = "./local.file"

ACCESS_KEY = "YOUR-ACCESS-KEY"
SECRET_KEY = "YOUR-SECRET-KEY"

# 初始化对象存储 API Handler
oss_api = speedycloud.create_object_storage_api(ACCESS_KEY, SECRET_KEY)

# 大文件分段上传，封装接口
oss_api.upload_big_data(BUCKET, OBJECT, FILE_PATH, {'x-amz-acl': "public-read"})
```

