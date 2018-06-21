# Examples

## 初始化对象存储 API Handler

```python
oss_api = speedycloud.create_object_storage_api(ACCESS_KEY, SECRET_KEY)
```

使用自己的秘钥替换`ACCESS_KEY`,`SECRET_KEY`

## 接口使用

### 获取 bucket 列表

```python
print oss_api.list("桶名")
```

更多接口调用示例，参照 `example.py`