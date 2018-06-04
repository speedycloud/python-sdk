import speedycloud

bucket_name = "bucketName"
key_name = "keyName"
file_path = "/root/abc.mp4"

cli = speedycloud.create_object_storage_api("access_key", "secret_key")

cli.upload_big_data(bucket_name, key_name, file_path, "file", {})
