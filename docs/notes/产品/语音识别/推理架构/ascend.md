[应用代码: Whisper, NLP, CV]
          │
          ▼
  MindSpore / MindNLP (高层框架)
          │
          ▼
  CANN Toolkit + Runtime (编译/调度/算子库)
          │
          ▼
  Ascend Driver + 固件
          │
          ▼
      Ascend NPU (310 / 910 / 310L Pro ...)
      |


问题
1 https://www.hiascend.com/forum/thread-0240174637177405027-1-1.html
您好，dcmi module initialize failed.ret is -8005  报错一般是安装的驱动未生效或未执行初始化，可以检查下相关的配套，另外建议更新到对应mindie适配版本的配套

另外，--privileged  这个参数 代表启动特权容器，不启动特权容器的时候 带-device 参数, 这种容器在整个开启的时段会锁住卡的使用权，特权容器有宿主机权限，可以无视其他--device容器的占用，按照先来后到的顺序临时使用，使用完释放；但是 --privileged 和--device 依然可以配合使用挂载指定的设备。


A-lucky:是的，找到原因了，说我用的那个mindie镜像必须使用那个特权容器才行
