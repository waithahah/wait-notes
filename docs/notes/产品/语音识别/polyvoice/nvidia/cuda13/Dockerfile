FROM nvidia/cuda:12.8.0-runtime-ubuntu22.04

# 设置环境变量
ENV PYTHONUNBUFFERED=1 \
    TZ=Asia/Shanghai \
    PYTHONPATH=/app \
    PATH="/usr/local/bin:/app/.venv/bin:$PATH" \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_INDEX_STRATEGY=unsafe-best-match

WORKDIR /app/

# 安装依赖并清理缓存
RUN apt-get update || true && \
    apt-get install -y --no-install-recommends \
    python3 python3-pip python3-dev gcc g++ curl make pkg-config \
    yasm nasm build-essential autoconf automake libtool \
    libx264-dev libx265-dev libvpx-dev libfdk-aac-dev \
    libmp3lame-dev libopus-dev libvorbis-dev libtheora-dev \
    libass-dev libfreetype6-dev libgnutls28-dev libsdl2-dev && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# 复制并编译FFmpeg源码
COPY ./docker/models/FFmpeg-master /tmp/ffmpeg-source
RUN cd /tmp/ffmpeg-source && \
    ./configure \
    --prefix=/usr/local \
    --enable-gpl \
    --enable-libass \
    --enable-libfdk-aac \
    --enable-libfreetype \
    --enable-libmp3lame \
    --enable-libopus \
    --enable-libvpx \
    --enable-libx264 \
    --enable-libx265 \
    --enable-nonfree && \
    make -j$(nproc) && \
    make install && \
    ldconfig && \
    rm -rf /tmp/ffmpeg-source

COPY --from=ghcr.io/astral-sh/uv:0.9.2 /uv /uvx /bin/

COPY ./pyproject.toml ./uv.lock /app/

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --extra gpu && \
    uv pip uninstall onnxruntime numpy && \
    uv pip install --no-cache-dir onnxruntime-gpu==1.22.0 clearvoice==0.1.2

COPY ./docker/models/1/* /root/.cache/modelscope/hub/models/iic
COPY ./docker/models/2/deepdml /app/models/2/deepdml
COPY ./docker/models/3/polyvoice_3/. /root/.cache/dolphin/
COPY ./docker/models/3/cmudict.zip /root/nltk_data/corpora/cmudict.zip
COPY ./docker/models/3/averaged_perceptron_tagger.zip /root/nltk_data/taggers/averaged_perceptron_tagger.zip
COPY ./docker/models/sd/speaker /app/models/sd
COPY ./docker/gitbub_asr_editing_records/dolphin/transcribe.py /app/.venv/lib/python3.10/site-packages/dolphin/transcribe.py
COPY ./docker/models/checkpoints /app/checkpoints
COPY ./docker/gitbub_asr_editing_records/clearvoice/networks.py /app/.venv/lib/python3.10/site-packages/clearvoice/networks.py

COPY ./app /app/app

EXPOSE 8010

ENV LD_LIBRARY_PATH=/app/.venv/lib/python3.10/site-packages/nvidia/cudnn/lib:$LD_LIBRARY_PATH

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8010"]

