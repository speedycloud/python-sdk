import speedycloud

bucket_name = "wsx"
key_name = "keyName"
file_path = "/home/wsx/Desktop/ssss.mov"

cli = speedycloud.create_object_storage_api("FC12640FE92A7", "f2315283a18e0c7dc835ed32b4cad42e5d9206a7e0c79")

cli.upload_big_data(bucket_name, key_name, file_path, "file", {})
