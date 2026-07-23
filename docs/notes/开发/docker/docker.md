1. 清理 Docker 占用的空间
运行以下命令释放 Docker 占用的磁盘空间：

bash
复制
编辑
docker system prune -a --volumes



下一步：把这个地址配置进 Docker 守护进程
编辑配置文件：

bash
复制
编辑
mkdir -p /etc/systemd/system/docker.service.d
nano /etc/systemd/system/docker.service.d/http-proxy.conf
添加以下内容（根据你上面的测试）：

ini
复制
编辑
[Service]
Environment="HTTP_PROXY=http://172.21.43.112:12334"
Environment="HTTPS_PROXY=http://172.21.43.112:12334"
Environment="NO_PROXY=localhost,127.0.0.1"
然后执行：

bash
复制
编辑
systemctl daemon-reexec
systemctl daemon-reload
systemctl restart docker


## 验证
```bash
docker run -it --rm   --gpus device=3   -v /usr/local/cuda-12.8/compat:/opt/nvidia/compat:ro   -e NVIDIA_DISABLE_REQUIRE=true   -e LD_LIBRARY_PATH=/opt/nvidia/compat   -e CUDA_VISIBLE_DEVICES=0   -e NVIDIA_VISIBLE_DEVICES=3   polynex/poly-voice:5.0.0 /bin/bash
```


3.2 多架构镜像构建
支持不同CPU架构的镜像构建：

# 使用buildx构建多架构镜像
docker buildx create --name multiarch
docker buildx use multiarch
 
# 构建并推送多架构镜像
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --tag your-username/docker-demo:latest \
  --push .