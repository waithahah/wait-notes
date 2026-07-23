# UV

## window PowerShell 激活虚拟环境脚本执行策略设置为 RemoteSigned：
PS E:\github2\NexOmni\backend> Set-ExecutionPolicy -Scope Process RemoteSigned
PS E:\github2\NexOmni\backend> .venv\Scripts\Activate.ps1

## 常用命令

### 创建虚拟环境

- uv venv --python 3.12

### 安装和管理 Python 本身

- uv python install：安装 Python 版本。
- uv python list：查看可用的 Python 版本。
- uv python find：查找已安装的 Python 版本。
- uv python pin：将当前项目固定为使用特定的 Python 版本。
- uv python uninstall：卸载 Python 版本。

### 安装特定版本的python

- uv python install 3.12 : 安装指定版本的 Python 3.12 版本。
- uv python install --reinstall : 这将重新安装所有先前安装的 Python 版本。
- uv python list ：要查看可用和已安装的 Python 版本

### 创建和处理 Python 项目，即带有 pyproject.toml 的项目

- uv init：创建一个新的 Python 项目。
- uv add：向项目添加依赖项。
- uv remove：从项目中删除依赖项。
- uv sync：将项目的依赖项与环境同步。
- uv lock：为项目的依赖项创建锁文件。
- uv run：在项目环境中运行命令。
- uv tree：查看项目的依赖关系树。
- uv build：将项目构建为分发归档。
- uv publish：将项目发布到包索引。

### 管理和检查 uv 的状态，例如缓存、存储目录或执行自我更新

- uv cache clean：删除缓存条目。
- uv cache prune：删除过时的缓存条目。
- uv cache dir：显示 uv 缓存目录路径。
- uv tool dir：显示 uv 工具目录路径。
- uv python dir：显示 uv 已安装的 Python 版本路径。
- uv self update：将 uv 更新到最新版本。

## 项目环境运行命令

- uv run python -c "import example"

## 锁定与同步

- uv lock : 锁定（Locking）是将项目依赖解析到 锁文件（lockfile） 的过程。

- uv sync : 同步（Syncing）是从锁文件中安装一部分包到 项目环境 的过程。它将删除锁文件中不存在的任何包。

- uv sync --inexact : 保留无关的包,同步默认是“精确的”，这意味着它将删除锁文件中不存在的任何包。

## 互斥可选

- uv sync --no-default-groups --extra cpu
- uv sync --no-default-groups --extra asr
- uv sync --no-default-groups --extra ai_asr
