# github 配置 ssh

## 生成密钥

```bash
ssh-keygen -t rsa -C "waithahah@gmail.com"
```

## 复制公钥

```bash
cat ~/.ssh/id_rsa.pub
```

## 彻底还原所有本地改动（危险操作）

    这个会让你的代码恢复到最近一次 git pull 或 git clone 后的状态，所有本地更改都会被清除，包括未添加进 Git 的新文件！

    bash
    复制
    编辑
    git reset --hard HEAD
    git clean -fd

## 配置单个仓库的邮箱账号

git config user.name "waithahah"
git config user.email "waithahah@gmail.com"


## 突然更新不了解决方案

方法一：手动将主机密钥添加到 known_hosts
这是最直接的方法：

删除旧的 github.com 记录（如果存在）：

ssh-keygen -R github.com
ssh-keygen -R ssh.github.com
ssh-keygen -R [ssh.github.com]:443
ssh-keyscan -t rsa,ed25519 -p 443 ssh.github.com >> ~/.ssh/known_hosts
grep "ssh.github.com" ~/.ssh/known_hosts

你好！这是一个非常常见的企业网络环境问题，很多公司出于安全考虑，会封锁或限制对常用端口（如 GitHub 的 443 和 22）的访问。

别担心，有几种方法可以尝试解决这个问题。

方法一：使用 SSH 替代 HTTPS（但需要更改端口）
这是最推荐和“正确”的解决方案。GitHub 允许通过 SSH 在端口 443 上进行连接。这招通常能绕过公司防火墙，因为防火墙一般不会阻断所有 443 端口的流量（HTTPS 流量就在这个端口）。

步骤如下：

检查你是否已使用 SSH 协议：
首先，查看你的远程仓库地址。

bash
git remote -v
如果显示的是 https://github.com/...，你需要将其改为 SSH 格式。

将远程 URL 更改为 SSH 格式：

bash
git remote set-url origin git@github.com:waithahah/node.git
（请将 waithahah/node.git 替换为你的实际用户名和仓库名）

创建或修改 SSH 配置：
在你的用户主目录下（~/.ssh 在 Linux/macOS 上，C:\Users\你的用户名\.ssh 在 Windows 上），创建或修改 config 文件。
添加以下内容：

Host github.com
  Hostname ssh.github.com
  Port 443
  User git
这个配置告诉 SSH 客户端，所有连接到 github.com 的请求，实际都转向 ssh.github.com 的 443 端口。

再次尝试推送：

bash
git push origin main
第一次连接时可能会询问你是否信任主机密钥，输入 yes 即可。