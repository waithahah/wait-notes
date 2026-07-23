# Ubuntu 22.04 LTS 系统配置指南

## 一、设置 root 用户密码并切换为 root

### 1. 设置 root 密码

如果尚未设置 root 密码，执行以下命令：

```bash
sudo passwd root
```

按提示输入两次新密码。

### 2. 切换为 root 用户

临时切换到 root 用户：

```bash
su -
```

输入刚才设置的 root 密码。

### 3. 配置 SSH root 登录（可选）

如果需要远程使用 root 登录，需要进行以下配置：

1. 编辑 SSH 配置文件：

```bash
nano /etc/ssh/sshd_config
```

1. 修改或添加以下配置项：

```conf
PermitRootLogin yes
PasswordAuthentication yes
```

1. 重启 SSH 服务使配置生效：

```bash
systemctl restart sshd
```

## 查看磁盘占用情况

```bash
df -h
```
### 查看某个目录占用大小
```bash
du -sh /目录
```
### 查看当前目录下所有子目录占用大小并排序
```bash
du -sh * | sort -h
```
