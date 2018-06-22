# -*- coding: utf-8 -*-

import os
import urllib
from lxml import etree

from speedycloud.object_storage import AbstractProductAPI


class ObjectStorageAPI(AbstractProductAPI):
    BASE_PATH = '/'

    def _get_path(self, suffix):
        return "%s%s" % (self.BASE_PATH, suffix)

    def list(self, bucket, prefix=""):
        """
        查询桶内对象列表
        参数:
            bucket: 桶名
        注意： bucket参数为''时，可查看所有桶
        """
        path = self._get_path('%s?prefix=%s' % (bucket, prefix))
        return self.get(path)

    def get_services(self):
        """
        获取桶列表
        :return: 桶列表
        """
        path = self._get_path("")
        return self.get(path)

    def create_bucket(self, bucket):
        """
        创建存储桶
        参数:
            bucket: 桶名
        """
        path = self._get_path('%s' % bucket)
        return self.put(path)

    def delete_bucket(self, bucket):
        """
        注意： 在桶内没有对象的时候才能删除桶
        删除存储桶
        参数:
            bucket: 桶名
        """
        path = self._get_path('%s' % bucket)
        return self.delete(path)

    def query_bucket_acl(self, bucket):
        """
        查询桶的权限
        参数:
            bucket: 桶名
        """
        path = self._get_path('%s?acl' % bucket)
        return self.get(path)

    def query_object_acl(self, bucket, key):
        """
        查询桶内对象的权限
        参数:
            bucket: 桶名
            key: 对象名
        """
        path = self._get_path('%s/%s?acl' % (bucket, key))
        return self.get(path)

    def delete_object_data(self, bucket, key):
        """
        删除桶内非版本管理对象
        注意： 删除成功返回 HTTP 204
        参数:
            bucket: 桶名
            key: 对象名
        """
        path = self._get_path('%s/%s' % (bucket, key))
        return self.delete(path)

    def delete_versioning_object(self, bucket, key, versionId):
        """
        删除桶内版本管理对象
        :param bucket: 桶名
        :param key: 对象名
        :param versionId: 对象名
        :return:
        """
        path = self._get_path("%s/%s?versionId=%s" % (bucket, key, versionId))
        return self.delete(path)

    def configure_versioning(self, bucket, status):
        """
        设置版本控制
        :param bucket: 桶名
        :param status: 状态("Enabled"或者"Suspended")
        :return:
        """
        path = self._get_path("%s?versioning" % bucket)
        versioning_body = """<?xml version="1.0" encoding="UTF-8"?>
        <VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
          <Status>%s</Status>
        </VersioningConfiguration>"""
        body = versioning_body % status
        return self.put(path, data=body)

    def get_bucket_versioning(self, bucket):
        """
        查看当前桶的版本控制信息
        返回桶的状态（"Enabled"或者"Suspended"或者""）
        """
        path = self._get_path("%s?versioning" % bucket)
        return self.get(path)

    def get_object_versions(self, bucket):
        """
        获取当前桶内的所有对象的所有版本信息
        """
        path = self._get_path("%s?versions" % bucket)
        return self.get(path)

    def download_object_data(self, bucket, key):
        """
        下载桶内对象的数据
        参数:
            bucket: 桶名
            key: 对象名
        """
        path = self._get_path('%s/%s' % (bucket, key))
        return self.get(path)

    def update_bucket_acl(self, bucket, header_params=None):
        """
        修改桶的权限
        参数:
            bucket: 桶名
            header_params: 请求头参数， 是一个字典
                {'x-amz-acl':test}
                    test: 允许值
                        private：自己拥有全部权限，其他人没有任何权限
                        public-read：自己拥有全部权限，其他人拥有读权限
                        public-read-write：自己拥有全部权限，其他人拥有读写权限
                        authenticated-read：自己拥有全部权限，被授权的用户拥有读权限
        """
        if header_params is None:
            header_params = {}
        path = self._get_path('%s?acl' % bucket)
        return self.put(path, params=header_params)

    def update_object_acl(self, bucket, key, header_params=None):
        """
        修改桶内对象的权限
        参数:
            bucket: 桶名
            key: 对象名
            header_params: 请求头参数， 是一个字典
                {'x-amz-acl':test}
                    test: 允许值
                        private：自己拥有全部权限，其他人没有任何权限
                        public-read：自己拥有全部权限，其他人拥有读权限
                        public-read-write：自己拥有全部权限，其他人拥有读写权限
                        authenticated-read：自己拥有全部权限，被授权的用户拥有读权限
        """

        if header_params is None:
            header_params = {}
        path = self._get_path('%s/%s?acl' % (bucket, urllib.quote(key)))
        return self.put(path, params=header_params)

    def update_versioning_object_acl(self, bucket, key, versionId, header_params=None):
        """
        修改桶内版本管理对象的权限
        参数:
            bucket: 桶名
            key: 对象名
            versionId: 对象版本号
            header_params: 请求头参数， 是一个字典
                {'x-amz-acl':test}
                    test: 允许值
                        private：自己拥有全部权限，其他人没有任何权限
                        public-read：自己拥有全部权限，其他人拥有读权限
                        public-read-write：自己拥有全部权限，其他人拥有读写权限
                        authenticated-read：自己拥有全部权限，被授权的用户拥有读权限
        """

        if header_params is None:
            header_params = {}
        path = self._get_path('%s/%s?acl&versionId=%s' %
                              (bucket, urllib.quote(key), versionId))
        return self.put(path, params=header_params)

    def storing_object_data(self, bucket, key, update_data, update_type, header_params=None):
        """
        创建存储桶内对象
        参数:
            bucket: 桶名
            key: 对象名
            update_data: 对象的内容（文件的路径/字符串）
            update_type: 对象内容类型 允许值 'file','string'
        """
        global update_content
        if header_params is None:
            header_params = {}
        path = self._get_path('%s/%s' % (bucket, urllib.quote(key)))
        if update_type == 'data':
            update_content = update_data
        if update_type == 'file':
            update_content = open(str(update_data), 'rb').read()
        elif update_type == 'string':
            update_content = update_data
        return self.put(path, update_content, params=header_params)

    def initiate_multipart_upload(self, bucket, key, params=None):
        """
        上传大数据第一步,初始化分段上传
        参数:
            bucket: 桶名
            key: 对象名
        """
        if params is None:
            params = {}
        path = self._get_path('%s/%s?uploads' % (bucket, key))
        xml = self.post(path, params=params)
        root = etree.fromstring(xml)
        upload_id = root.find(
            ".//{http://s3.amazonaws.com/doc/2006-03-01/}UploadId").text
        return upload_id

    def upload_part(self, bucket, key, update_data, part_number, upload_id):
        """
        上传大数据第二步，上传分段
        参数:
            bucket: 桶名
            key: 对象名
            update_data: 对象的内容（文件的路径/字符串）
            update_type: 对象内容类型 允许值 'file','string'
            part_number: 上传的第几部分，分几部分就运行几次本函数
            upload_id: 上传大数据第一步返回的uploadID
        注意：将返回的etag保存，在大数据上传第三步使用
        """
        path = self._get_path('%s/%s?partNumber=%s&uploadId=%s' % (
            bucket, key, int(part_number), str(upload_id)))
        request, header = self.upload_big_data_put(path, update_data)
        return self.parse_header(header)

    @staticmethod
    def parse_header(header):
        for info in header:
            if info[0] == "etag":
                return info[1]
        return ""

    def complete_multipart_upload(self, bucket, key, update_data, update_type, upload_id):
        """
        上传大数据第三步,完成分段上传
        参数:
            bucket: 桶名
            key: 对象名
            update_data: 对象的内容（文件的路径/字符串）
            update_type: 对象内容类型 允许值 'file','string'
            upload_id: 上传大数据第一步返回的uploadID
        """
        global update_content
        path = self._get_path('%s/%s?uploadId=%s' %
                              (bucket, key, str(upload_id)))
        if update_type == 'file':
            update_content = open(str(update_data), 'rb').read()
        elif update_type == 'string':
            update_content = update_data
        return self.post(path, update_content)

    def upload_big_data(self, bucket, key, update_data, params):
        """
        上传大数据第三步,完成分段上传
        参数:
            bucket: 桶名
            key: 对象名
            update_data: 对象的内容（文件的路径/字符串）
            params: 参数，例如 Content-Type
        """
        uid = self.initiate_multipart_upload(bucket, key, params)
        with open(update_data) as f:
            length = os.path.getsize(update_data)
            # DEFAULT FILE SIZE
            if length > 64 * 1024 * 1024 * 1024:
                print "file is bigger than 64G"
                return
            i = length / (1024 * 1024 * 20)
            j = length % 1024 * 1024 * 20
            if j != 0:
                i += 1
            s = ""
            for k in range(i):
                if k != i - 1:
                    etag = self.upload_part(bucket, key, f.read(1024 * 1024 * 20), k + 1, uid)
                else:
                    etag = self.upload_part(bucket, key, f.read(length - k * 1024 * 1024 * 20),
                                            k + 1, uid)
                s += '<Part><PartNumber>%s</PartNumber><ETag>%s</ETag></Part>' % (k + 1, etag)

        s = '<CompleteMultipartUpload>' + s + '</CompleteMultipartUpload>'
        path = self._get_path('%s/%s?uploadId=%s' % (bucket, key, uid))
        return self.post(path, data=s, params=params)
