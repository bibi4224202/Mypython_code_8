 # 定义音乐文件夹路径（根据实际情况修改）
        music_folder = "music"
        f=os.listdir(music_folder)

        # 获取所有MP3文件名并存入列表
        #os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
        lis = [
            filename for filename in os.listdir(music_folder)
            if filename.lower().endswith(".mp4")
        ]

        # 可选：按文件名排序
        songList = sorted(lis)

        # 去除后缀的两种方法
        # 方法一：使用os.path模块（推荐）
        song = [os.path.splitext(filename)[0] for filename in songList]

        # 方法二：字符串切割
        #song = [filename.rsplit(".", 1)[0] for filename in songList]#用第一个.分割
        #song = [filename.split(".")[0] for filename in songList]

        print("请输入歌曲名：")
        for songname in song:
            print('*   '+songname)
