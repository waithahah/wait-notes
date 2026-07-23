echo "=============================="
echo "2. 更新系统并安装依赖"
echo "=============================="
apt update && apt install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

echo "=============================="
echo "3. 添加 Docker GPG 密钥"
echo "=============================="
mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
    | gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo "=============================="
echo "4. 添加 Docker APT 源"
echo "=============================="
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" \
  > /etc/apt/sources.list.d/docker.list

echo "=============================="
echo "5. 安装 Docker Engine 和 Compose"
echo "=============================="
apt update && apt install -y \
    docker-ce \
    docker-ce-cli \
    containerd.io \
    docker-buildx-plugin \
    docker-compose-plugin

echo "=============================="
echo "6. 启动 Docker 并设置开机自启"
echo "=============================="
systemctl enable docker
systemctl start docker

echo "=============================="
echo "7. 验证 Docker 安装"
echo "=============================="
docker version
docker compose version
