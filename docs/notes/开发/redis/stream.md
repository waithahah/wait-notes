# redis stream 消息队列

## 消息队列

### 生产者

### 消费者

## 消费组

### 基本命令

- 创建消费者组

```bash
    XGROUP CREATE stream:audio.extract.completed group1 0-0
```

- 查看消费者组

```bash
    XINFO GROUPS stream:video.extract.completed
```

- 查看消费者组信息

```bash
    XINFO CONSUMERS stream:video.extract.completed video_extract_image_classification_completed_nex_group
```

- 删除消费组

```bash
    XGROUP DESTROY stream:video.extract.completed video_extract_image_classification_completed_nex_group
```

## 消费者
- 删除消费者

```bash
    XGROUP DELCONSUMER stream:audio.extract.completed group1 consumer1
```
## 基本命令



## 注意
消费者空闲时间是按收到任务后才重置