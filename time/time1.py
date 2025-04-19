import time
import sys

def static_time():
    try:
        while True:
            current_time = time.strftime("%H:%M:%S")
            # 直接覆盖当前行内容（\r实现光标复位）
            sys.stdout.write("\r" + current_time)
            sys.stdout.flush()
            time.sleep(0.1)  # 保持0.1秒刷新频率
    except KeyboardInterrupt:
        print("\n程序已退出")

if __name__ == "__main__":
    static_time()
