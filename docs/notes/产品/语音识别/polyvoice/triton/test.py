import sys
import os
import tritonclient.grpc as grpcclient
import numpy as np


import librosa
import numpy as np


def load_wav_any_format(path, target_sr=16000):
    """
    加载任意格式音频，并转换为 float32 单声道 16kHz
    """
    # librosa 会自动解码所有常见音频格式
    data, sr = librosa.load(path, sr=target_sr, mono=True)

    return data.astype(np.float32), target_sr


def main():
    # 支持通过命令行传入 wav 路径，否则使用相对路径 test_wavs/long.wav
    if len(sys.argv) > 1:
        wav_path = sys.argv[1]
    else:
        wav_path = os.path.join(os.path.dirname(__file__), "test_wavs", "10分钟.opus")

    if not os.path.exists(wav_path):
        print(f"WAV 文件不存在: {wav_path}")
        sys.exit(1)

    waveform, sr = load_wav_any_format(wav_path, target_sr=16000)
    print(f"Loaded {wav_path}, resampled to {sr}, samples={waveform.shape[0]}")

    # 可选：从命令行获取语言和文本规范化选项（第二、第三个参数）
    # usage: python test.py /path/to/long.wav [language] [text_norm]
    language = sys.argv[2] if len(sys.argv) > 2 else "zh"
    text_norm = sys.argv[3] if len(sys.argv) > 3 else "none"

    # Triton 一般期望的输入是形状 (1, T)
    waveform = waveform.reshape(1, -1)
    lengths = np.array([[waveform.shape[1]]], dtype=np.int32)

    # 连接到 Triton 服务器
    triton_client = grpcclient.InferenceServerClient(
        url="localhost:8084",
        verbose=False,
    )

    if triton_client.is_server_live():
        print("Triton 服务器运行正常")

    # 创建推理请求
    # 有些模型还需要额外的字符串输入，例如 LANGUAGE、TEXT_NORM 等，类型为 BYTES
    inputs = [
        grpcclient.InferInput("WAV", waveform.shape, "FP32"),
        grpcclient.InferInput("WAV_LENS", lengths.shape, "INT32"),
        grpcclient.InferInput("LANGUAGE", (1, 1), "INT32"),
        grpcclient.InferInput("TEXT_NORM", (1, 1), "INT32"),
    ]
    inputs[0].set_data_from_numpy(waveform)
    inputs[1].set_data_from_numpy(lengths)

    # BYTES 类型需要用 numpy object array（bytes）传入
    # LANGUAGE 期望 INT32：尝试将用户传入的语言字符串映射为整数或直接使用数字
    try:
        lang_val = int(language)
    except Exception:
        lang_map = {
            "zh": 0,
            "cn": 0,
            "chinese": 0,
            "zh-cn": 0,
            "en": 1,
            "eng": 1,
            "english": 1,
        }
        lang_val = lang_map.get(language.lower(), 0)
    lang_arr = np.array([[lang_val]], dtype=np.int32)
    # TEXT_NORM 期望 INT32，尝试把用户传入的字符串转换为 int
    try:
        tn_val = int(text_norm)
    except Exception:
        mapping = {
            "none": 0,
            "false": 0,
            "no": 0,
            "true": 1,
            "yes": 1,
            "lowercase": 1,
            "normalize": 1,
        }
        tn_val = mapping.get(text_norm.lower(), 0)
    text_norm_arr = np.array([[tn_val]], dtype=np.int32)
    inputs[2].set_data_from_numpy(lang_arr)
    inputs[3].set_data_from_numpy(text_norm_arr)

    outputs = [grpcclient.InferRequestedOutput("TRANSCRIPTS")]

    # 发送推理请求（根据你的 Triton 模型名调整 model_name）
    response = triton_client.infer(
        model_name="sensevoice",
        inputs=inputs,
        outputs=outputs,
    )

    # 获取并打印结果
    transcripts = response.as_numpy("TRANSCRIPTS")
    if transcripts is None:
        print("没有返回 TRANSCRIPTS 输出，请检查模型配置")
        return

    # 结果通常是 bytes 数组
    result = transcripts[0]
    if isinstance(result, (bytes, bytearray)):
        print(result.decode("utf-8"))
    else:
        # 如果是 numpy 字符串类型
        try:
            print(result.astype("U").item())
        except Exception:
            print(result)


if __name__ == "__main__":
    main()
