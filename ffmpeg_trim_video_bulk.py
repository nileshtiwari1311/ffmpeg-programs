import os
import time

base_episode_number = 1
no_of_episodes = 94

for i in range(0, no_of_episodes) :
	os.system('ffmpeg -hide_banner -i myVideo_' + str(i+base_episode_number) + '.mp4 -ss 00:00:25 -c:v copy -c:a copy E' + str(i+base_episode_number) + '.mp4')
	time.sleep(4)