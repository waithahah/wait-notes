# docker
## 列出标签为none的镜像
```bash
docker images -f "dangling=true" --format "{{.ID}}\t{{.Repository}}:{{.Tag}}"
```

```bash
docker images -f "dangling=true
```

## 删除标签为none的镜像
```bash
docker rmi $(docker images -f "dangling=true" -q)
```

# docker compose

## 构建镜像

```bash
    docker-compose build
    docker build -t <镜像名>:<标签> <Dockerfile所在路径>
```
