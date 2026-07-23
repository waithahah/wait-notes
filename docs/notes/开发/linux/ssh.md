配置 SSH 免密登录（公钥认证）可以让你无需输入密码即可登录远程服务器。以下是详细步骤：

1. 本地生成 SSH 密钥对
在本地机器上生成公钥和私钥：

bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
-t rsa：指定密钥类型为 RSA。

-b 4096：指定密钥长度为 4096 位（更安全）。

-C：添加注释（可选，通常用邮箱标识）。

按提示操作：

默认保存路径为 ~/.ssh/id_rsa（直接按回车）。

设置密钥密码（可选，直接回车跳过）。

2. 将公钥上传到远程服务器
方法一：使用 ssh-copy-id（推荐）
bash
ssh-copy-id -i ~/.ssh/id_rsa.pub username@remote_host
输入远程服务器的密码，完成后公钥会自动添加到 ~/.ssh/authorized_keys。

方法二：手动复制（若无 ssh-copy-id）
查看本地公钥：

bash
cat ~/.ssh/id_rsa.pub
登录远程服务器：

bash
ssh username@remote_host
在远程服务器上创建 .ssh 目录（若不存在）：

bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
将公钥添加到 authorized_keys：

bash
echo "粘贴的公钥内容" >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
3. 测试免密登录
bash
ssh username@remote_host
如果配置成功，将直接登录，无需输入密码。

4. 常见问题排查
权限问题：

确保远程服务器上的目录和文件权限：

bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
SSH 配置检查：

确保远程服务器的 /etc/ssh/sshd_config 包含：

text
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
修改后重启 SSH 服务：

bash
sudo systemctl restart sshd  # Linux
sudo service ssh restart    # 其他系统
密钥路径问题：

如果使用非默认密钥路径，需在 ~/.ssh/config 中指定：

text
Host remote_host
    IdentityFile ~/.ssh/custom_key
5. 进阶配置（可选）
禁用密码登录（增强安全）：
在远程服务器的 /etc/ssh/sshd_config 中设置：

text
PasswordAuthentication no
重启 SSH 服务后，仅允许密钥登录。

多台服务器管理：
在本地 ~/.ssh/config 中配置别名：

text
Host server1
    HostName remote_host1
    User username
    IdentityFile ~/.ssh/id_rsa
之后可直接用 ssh server1 登录。

通过以上步骤，你已成功配置 SSH 免密登录。如果遇到问题，检查日志：

bash
tail -f /var/log/auth.log  # Linux 系统