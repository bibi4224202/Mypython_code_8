import tkinter as tk
import time




lass BigClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)  # 全屏显示
        self.root.configure(bg='black')

        # 创建时间标签
        self.time_label = tk.Label(
            self.root,
            font=('Arial', 72),  # 字号设置为72
            fg='white',
            bg='black'
        )
        self.time_label.pack(expand=True)

        # 绑定退出快捷键
        self.root.bind('<Escape>', lambda e: self.root.destroy())

        self.update_time()  # 启动时间更新

    def update_time(self):
        current_time = time.strftime("现在时间是：\n%Y-%m-%d %H:%M:%S")
        self.time_label.config(text=current_time)
        self.root.after(200, self.update_time)  # 每200ms更新一次


if __name__ == "__main__":
    clock = BigClock()
    clock.root.mainloop()
