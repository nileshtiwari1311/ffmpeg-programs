import os
os.system('ffmpeg -hide_banner -i myVideo.mp4 -ss 00:00:25 -c:v copy -c:a copy myVideo-trimmed.mp4')