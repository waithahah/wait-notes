import json
import os

import openpyxl
import requests

# =============================
# 配置区域
# =============================
AUDIO_DIR = r"E:\测试文件\音频\zh-中文\河南话\377Hours_HenanDialectConversationalSpeechDataByMobilePhone"  # 音频文件目录
API_URL = "http://36.248.221.176:8010/v1/voice/stt"
OUTPUT_EXCEL = "stt_compare.xlsx"


def call_whisper_stt_api(audio_path):
    """使用 requests 调用本地 STT 接口并返回识别文本"""
    try:
        with open(audio_path, "rb") as f:
            files = {"audio_file": (os.path.basename(audio_path), f, "audio/wav")}

            response = requests.post(API_URL, files=files, timeout=30)

        # 如果返回 JSON
        try:
            data = response.json()
            data = data["data"]
            return data.get("text", "").strip()
        except json.JSONDecodeError:
            # 若不是 JSON，直接返回文本
            return response.text.strip()

    except Exception as e:
        return f"API 请求失败: {e}"


def call_sensevoice_stt_api(audio_path):
    """使用 requests 调用本地 STT 接口并返回识别文本"""
    try:
        with open(audio_path, "rb") as f:
            files = {"audio_file": (os.path.basename(audio_path), f, "audio/wav")}
            payload = {"asr_model": "1"}
            response = requests.post(API_URL, files=files, data=payload, timeout=30)

        # 如果返回 JSON
        try:
            data = response.json()
            data = data["data"]
            return data.get("text", "").strip()
        except json.JSONDecodeError:
            # 若不是 JSON，直接返回文本
            return response.text.strip()

    except Exception as e:
        return f"API 请求失败: {e}"


def call_dolphin_stt_api(audio_path):
    """使用 requests 调用本地 STT 接口并返回识别文本"""
    try:
        with open(audio_path, "rb") as f:
            files = {"audio_file": (os.path.basename(audio_path), f, "audio/wav")}
            payload = {"asr_model": "3"}
            response = requests.post(API_URL, files=files, data=payload, timeout=30)

        # 如果返回 JSON
        try:
            data = response.json()
            data = data["data"]
            return data.get("text", "").strip()
        except json.JSONDecodeError:
            # 若不是 JSON，直接返回文本
            return response.text.strip()

    except Exception as e:
        return f"API 请求失败: {e}"


def read_txt(txt_path):
    """读取真实文本文件内容"""
    try:
        with open(txt_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception as e:
        return f"文本读取失败: {e}"


def compare_text(a, b):
    """简单字符级相似度：一致字符 / 长度"""
    if not a or not b:
        return 0
    same = sum(1 for x, y in zip(a, b) if x == y)
    return round(same / max(len(a), len(b)), 4)


# def main():
#     # 创建 Excel
#     wb = openpyxl.Workbook()
#     ws = wb.active
#     ws.title = "语音识别对比"
#     ws.append(["语音文件", "准确内容", "sensenvoice", "whisper"])

#     # 遍历所有 wav 文件
#     for file in os.listdir(AUDIO_DIR):
#         if file.lower().endswith(".wav"):
#             wav_path = os.path.join(AUDIO_DIR, file)
#             txt_path = wav_path.replace(".wav", ".txt")

#             print(f"处理：{file}")
#             stt_text = call_whisper_stt_api(wav_path)
#             stt_sensevoice_text = call_sensevoice_stt_api(wav_path)
#             real_text = read_txt(txt_path)

#             ws.append([file, real_text, stt_sensevoice_text, stt_text])

#     wb.save(OUTPUT_EXCEL)
#     print(f"\n处理完成，结果已导出: {OUTPUT_EXCEL}")


def main():
    # 创建 Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "语音识别对比"
    ws.append(["语音文件", "准确内容", "dolphin", "whisper"])

    # 遍历所有 wav 文件
    for file in os.listdir(AUDIO_DIR):
        if file.lower().endswith(".wav"):
            wav_path = os.path.join(AUDIO_DIR, file)
            txt_path = wav_path.replace(".wav", ".txt")

            print(f"处理：{file}")
            stt_text = call_whisper_stt_api(wav_path)
            stt_dolphin_text = call_dolphin_stt_api(wav_path)
            real_text = read_txt(txt_path)

            ws.append([file, real_text, stt_dolphin_text, stt_text])

    wb.save(OUTPUT_EXCEL)
    print(f"\n处理完成，结果已导出: {OUTPUT_EXCEL}")


if __name__ == "__main__":
    main()
