import os

# 定义音乐文件夹路径（根据实际情况修改）
music_folder = "music"
f=os.listdir(music_folder)

# 获取所有MP3文件名并存入列表
#os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
lis = [
    filename for filename in os.listdir(music_folder)
    if filename.lower().endswith(".mp3")
]

# 可选：按文件名排序
lis = sorted(lis)


# 打印结果验证
print("找到的MP3文件：")
for song in lis:
    print(f"• {song}")