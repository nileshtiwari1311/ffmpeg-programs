import os
import time
import glob

for file in glob.glob('*.mp4'):
	filename = os.path.splitext(file)[0]
	os.system('ffmpeg -hide_banner -sseof -3 -i ' + file.replace(' ', '\ ') + ' -vsync 0 -q:v 1 -update true ' + 'img-' + filename.replace(' ', '-') + '.jpg')
	print('\n' + '------- Done ' + file + '--------' + '\n')
	time.sleep(0.1)