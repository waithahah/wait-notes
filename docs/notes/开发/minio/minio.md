# 过滤文件并下载到本地
mc find myminio/polynex/upload_files/ --name "*.opus" | while read file; do
    mc cp "$file" ./downloaded-opus/
done


可以使用 mc（MinIO Client）快速下载桶内的文件夹，步骤如下：

安装 mc：

bash
复制
编辑
wget https://dl.min.io/client/mc/release/linux-amd64/mc
chmod +x mc
sudo mv mc /usr/local/bin/
配置 MinIO：

bash
复制
编辑
mc alias set myminio http://\<minio-host>\:\<port>\ \<access-key>\ \<secret-key>\
下载桶内文件夹：

bash
复制
编辑
mc cp --recursive myminio/\<bucket-name>\/\<folder-path>\ ./local-dir/