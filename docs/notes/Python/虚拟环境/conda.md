# Conda 基本使用命令

## 环境管理

### 创建环境

```bash
# 创建名为myenv的Python环境，指定Python版本
conda create --name myenv python=3.12

# 创建环境并安装指定包
conda create -n myenv numpy pandas
```

### 激活/停用环境

```bash
# 激活环境
conda activate myenv

# 停用当前环境
conda deactivate
```

### 查看环境

```bash
# 列出所有环境
conda env list

# 查看当前环境信息
conda info

which is python
```

### 删除环境

```bash
# 删除环境
conda env remove --name myenv
```

## 包管理

### 安装包

```bash
# 安装包
conda install numpy

# 安装指定版本的包
conda install numpy=1.19.2
```

### 查看包

```bash
# 列出当前环境安装的包
conda list

# 查看某个包的信息
conda search numpy
```

### 更新包

```bash
# 更新包
conda update numpy

# 更新所有包
conda update --all
```

### 删除包

```bash
# 删除包
conda remove numpy
```

## 其他实用命令

```bash
# 清理缓存
conda clean --all

# 更新conda本身
conda update conda

# 禁用 base 环境的自动激活
conda config --set auto_activate_base false
```
