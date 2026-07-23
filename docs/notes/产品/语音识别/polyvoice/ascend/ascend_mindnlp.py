import mindspore as ms
from mindnlp.transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import librosa
import numpy as np
import os

# 屏蔽 numpy 的警告
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="numpy.core.getlimits")

# 检查文件是否存在
file_path = "zh_5min.opus"
if not os.path.exists(file_path):
    print(f"错误：文件 {file_path} 不存在")
    print("当前目录文件列表:", os.listdir("."))
    exit()

# 设置设备
ms.context.set_context(device_target="Ascend")

model_id = "whisper-large-v3-turbo"

print("正在加载模型...")
model = AutoModelForSpeechSeq2Seq.from_pretrained(model_id)
processor = AutoProcessor.from_pretrained(model_id)

print("创建 pipeline...")
pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
)


def load_audio_file(file_path):
    """加载音频文件"""
    try:
        # 使用 librosa 加载音频
        audio_data, sample_rate = librosa.load(file_path, sr=16000, mono=True)

        return {"array": audio_data.astype(np.float32), "sampling_rate": sample_rate}
    except Exception as e:
        print(f"加载音频文件失败: {e}")
        return None


print("处理音频文件...")
try:
    # 手动加载音频
    audio_input = load_audio_file(file_path)

    if audio_input is None:
        print("音频加载失败")
        exit()

    print("进行语音识别...")

    # 添加语言参数来避免警告
    result = pipe(
        audio_input,
        return_timestamps=True,
        generate_kwargs={"language": "zh"},  # 如果是中文音频，使用 "zh"
        # 如果是英文音频，使用 "en"
        # generate_kwargs={"language": "en"}
    )

    print("识别结果:", result["text"])
    print(f"识别结果1:{result}")

except Exception as e:
    print("发生错误:", e)
    print("错误类型:", type(e).__name__)
    import traceback

    traceback.print_exc()
