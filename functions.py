from pytube import YouTube
import subprocess
import secrets
import os

def download_video(url):
    yt = YouTube(url)
    if (yt.length / 60) > 2:
        return 'Video too long', 404
    else:
        videoname = secrets.token_hex(16)
        audioname = secrets.token_hex(16)
        finalvideo = secrets.token_hex(16)
        yt.streams.filter(only_video=True, file_extension="mp4").first().download("media", videoname)
        yt.streams.filter(only_audio=True).first().download("media", audioname)
        subprocess.run("ffmpeg -i " + "media\\" + videoname + ".mp4" + " -i " + "media\\" + audioname + ".mp4" + " -c copy " + "media\\" + finalvideo + ".mp4")
        os.remove("media\\" + videoname + ".mp4")
        os.remove("media\\" + audioname + ".mp4")
        return "media\\" + finalvideo + ".mp4"
    
def download_audio(url):
    yt = YouTube(url)
    if (yt.length / 60) > 2:
        return 'Video too long', 404
    else:
        audioname = secrets.token_hex(16)
        finalaudio = secrets.token_hex(16)
        yt.streams.filter(only_audio=True, file_extension="mp4").first().download("media", audioname)
        subprocess.run("ffmpeg -i " + "media\\" + audioname + ".mp4 " + "media\\" + finalaudio + ".mp3")
        os.remove("media\\" + audioname + ".mp4")
        return "media\\" + finalaudio + ".mp3"