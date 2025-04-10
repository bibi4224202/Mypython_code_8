import pygame
import time

pygame.mixer.init()#创建一个音乐流pygame.mixer.init()#创建一个音乐流
'''
pygame.mixer.init()#创建一个音乐流

songName="赠卫八处士.mp3"
pygame.mixer.music.load(songName)#解析

pygame.mixer.music.set_volume(0.8)

pygame.mixer.music.play()
'''

songList=["让我们荡起双桨","听我说谢谢你","赠卫八处士","京口北固亭怀古"]
print("==========歌单============")
for i in songList:
    print("*   "+i)
print("=========================")

#2、接受用户点歌

#3、播放歌曲
while True:
    songName=input("你想听的歌曲是：")
    for name in songList:
        if songName==name:
           
            songName=name
            pygame.mixer.music.load('music/'+songName+".mp3")

            pygame.mixer.music.set_volume(0.8)

            pygame.mixer.music.play()
            #time.sleep(60)#延迟60秒
            #pygame.mixer.music.stop()
        elif songName=="京口北固亭怀古":
            songName="music/京口北固亭怀古.mp3"
            pygame.mixer.music.load(songName)
            pygame.mixer.music.set_volume(0.8)
            pygame.mixer.music.play()
            #time.sleep(60)#延迟60秒
            #pygame.mixer.music.stop()
