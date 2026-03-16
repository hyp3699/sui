import time
import random
import requests
import os

def main():
    # 随机等待 10~120 分钟（600~7200 秒）
    delay = random.randint(600, 7200)
    print(f"[INFO] 随机等待 {delay} 秒后开始访问网站")
    time.sleep(delay)

    # 访问目标网站
    url = os.getenv("TARGET_URL", "https://example.com")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    print(f"[INFO] 开始访问：{url}")
    try:
        resp = requests.get(url, headers=headers, timeout=20)
        print(f"[INFO] 状态码：{resp.status_code}")
        print("[INFO] 返回内容：")
        print(resp.text[:500])  # 防止输出太长
    except Exception as e:
        print(f"[ERROR] 请求失败：{e}")

if __name__ == "__main__":
    main()
  
