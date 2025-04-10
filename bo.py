
from moviepy.editor import VideoFileClip
import pygame
import sys
import os
import tempfile
import time


def play_video(video_path):
    """播放视频（含音频）并监听键盘事件（空格暂停/继续，Q退出）"""
    clip = VideoFileClip(video_path)
    has_audio = clip.audio is not None

    # 初始化音频系统
    temp_audio_path = None
    if has_audio:
        # 创建临时音频文件（显式关闭文件句柄）
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
            temp_audio_path = temp_audio.name

        # 确保音频文件写入完成
        clip.audio.write_audiofile(
            temp_audio_path,
            codec='pcm_s16le',  # WAV标准编码
            verbose=False,
            logger=None,
            ffmpeg_params=['-y']  # 覆盖已存在文件
        )

        # 等待文件写入完成
        while not os.path.exists(temp_audio_path) or os.path.getsize(temp_audio_path) == 0:
            time.sleep(0.1)

        pygame.mixer.init()
        pygame.mixer.music.load(temp_audio_path)
        pygame.mixer.music.play()

    # 初始化视频显示
    screen = pygame.display.set_mode(clip.size)
    clock = pygame.time.Clock()
    paused = False
    frame_generator = clip.iter_frames()

    try:
        for frame in frame_generator:
            # 处理事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = not paused
                        if has_audio:
                            if paused:
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.unpause()
                    elif event.key == pygame.K_q:
                        return False

            if not paused:
                # 显示视频帧
                frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
                screen.blit(frame_surface, (0, 0))
                pygame.display.flip()
                clock.tick(clip.fps)  # 保持视频帧率
            else:
                clock.tick(5)  # 暂停时降低刷新率

        return True
    finally:
        # 清理资源
        if has_audio:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
            try:
                os.remove(temp_audio_path)
            except:
                pass
        clip.close()
        pygame.display.quit()


def main():
    pygame.init()
    while True:

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



        video_path = 'music/'+input("\n请输入视频路径（输入 q 退出）: ").strip()+'.mp4'
        if video_path.lower() == "q":
            break

        if not os.path.exists(video_path):
            print("文件不存在，请重新输入！")
            continue

        print("播放中... 按空格暂停/继续，Q 退出当前视频")
        play_completed = play_video(video_path)
        if play_completed:
            print("播放完毕！")

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()