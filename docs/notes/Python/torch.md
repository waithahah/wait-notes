root@506150273e31:/app# stat /usr/lib/x86_64-linux-gnu/libcudnn_ops.so.9.0.0
  File: /usr/lib/x86_64-linux-gnu/libcudnn_ops.so.9.0.0
  Size: 108540440       Blocks: 212000     IO Block: 4096   regular file
Device: 3ch/60d Inode: 5644855     Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2024-02-03 23:32:21.000000000 +0000
Modify: 2024-02-03 23:32:21.000000000 +0000
Change: 2025-06-24 08:31:59.996933484 +0000
 Birth: 2025-06-24 08:31:59.500931482 +0000
root@506150273e31:/app# uv pip show ctranslate2
Name: ctranslate2
Version: 4.6.0
Location: /app/.venv/lib/python3.10/site-packages
Requires: numpy, pyyaml, setuptools
Required-by: faster-whisper
root@506150273e31:/app# ls -l /usr/lib/x86_64-linux-gnu/libcudnn_*.so*
lrwxrwxrwx 1 root root        21 Feb  3  2024 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9 -> libcudnn_adv.so.9.0.0
-rw-r--r-- 1 root root 239835264 Feb  3  2024 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.0.0
lrwxrwxrwx 1 root root        21 Feb  3  2024 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9 -> libcudnn_cnn.so.9.0.0
-rw-r--r-- 1 root root   4637288 Feb  3  2024 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.0.0
lrwxrwxrwx 1 root root        37 Feb  3  2024 /usr/lib/x86_64-linux-gnu/libcudnn_engines_precompiled.so.9 -> libcudnn_engines_precompiled.so.9.0.0
-rw-r--r-- 1 root root 573456920 Feb  3  2024 /usr/lib/x86_64-linux-gnu/libcudnn_engines_precompiled.so.9.0.0
lrwxrwxrwx 1 root root        42 Feb  3  2024 /usr/lib/x86_64-linux-gnu/libcudnn_engines_runtime_compiled.so.9 -> libcudnn_engines_runtime_compiled.so.9.0.0
-rw-r--r-- 1 root root  12833944 Feb  3  2024 /usr/lib/x86_64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.0.0
lrwxrwxrwx 1 root root        23 Feb  3  2024 /usr/lib/x86_64-linux-gnu/libcudnn_graph.so.9 -> libcudnn_graph.so.9.0.0
-rw-r--r-- 1 root root   2913120 Feb  3  2024 /usr/lib/x86_64-linux-gnu/libcudnn_graph.so.9.0.0
lrwxrwxrwx 1 root root        27 Feb  3  2024 /usr/lib/x86_64-linux-gnu/libcudnn_heuristic.so.9 -> libcudnn_heuristic.so.9.0.0
-rw-r--r-- 1 root root  87448976 Feb  3  2024 /usr/lib/x86_64-linux-gnu/libcudnn_heuristic.so.9.0.0
lrwxrwxrwx 1 root root        21 Feb  3  2024 /usr/lib/x86_64-linux-gnu/libcudnn_ops.so.9 -> libcudnn_ops.so.9.0.0
-rw-r--r-- 1 root root 108540440 Feb  3  2024 /usr/lib/x86_64-linux-gnu/libcudnn_ops.so.9.0.0
root@506150273e31:/app# uv pip show nvidia-cublas-cu12
Name: nvidia-cublas-cu12
Version: 12.1.3.1
Location: /app/.venv/lib/python3.10/site-packages
Requires:
Required-by: nvidia-cudnn-cu12, nvidia-cusolver-cu12, torch
root@506150273e31:/app# uv pip show nvidia-cudnn-cu12 
Name: nvidia-cudnn-cu12
Version: 9.1.0.70
Location: /app/.venv/lib/python3.10/site-packages
Requires: nvidia-cublas-cu12
Required-by: torch
root@506150273e31:/app# ls /app/.venv/lib/python3.10/site-packages/nvidia/cudnn/lib/libcudnn_ops.so.9
/app/.venv/lib/python3.10/site-packages/nvidia/cudnn/lib/libcudnn_ops.so.9






pip install --no-deps ./flash_attn-2.6.2+cu118torch2.0cxx11abiFALSE-cp310-cp310-linux_x86_64.whl
