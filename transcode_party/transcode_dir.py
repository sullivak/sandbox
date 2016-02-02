__author__ = 'sullivan'

import os
import shutil
import subprocess
import time
import datetime


base_dir = r'E:\Movies'
togo_dir = r'H:\MoviesOtherFormat'

dirs = filter(lambda x: os.path.isdir(os.path.join(base_dir, x)), os.listdir(base_dir))

cnt = 0
for dir in dirs:	
	whatsin = os.listdir(os.path.join(base_dir, dir))
	
	if 'VIDEO_TS.IFO' in whatsin or 'video_ts.ifo' in whatsin:		
		print 'shutil.move(r"' + os.path.join(base_dir, dir) + '", r"' + os.path.join(togo_dir, dir) + '")' 
		shutil.move(os.path.join(base_dir, dir), os.path.join(togo_dir, dir))
		# print 'move "' + os.path.join(base_dir, dir) + '" "' + os.path.join(togo_dir, dir) + '"'
		args = ['HandBrakeCLI', '-i', os.path.join(togo_dir, dir),
				'-o', os.path.join(base_dir, dir) + '.mp4',
				'-e', 'x264', '-q', '17', '--subtitle', 'scan,1,2,3,4,5,6,7,8,9,10', '-a', '1,2,3,4,5,6,7,8,9,10']
		#cmd_line = 'HandBrakeCLI -i "' + os.path.join(togo_dir, dir) + '" -o "' + os.path.join(base_dir, dir) + '.mp4"' + ' -e x264 -q 17 --subtitle scan,1,2,3,4,5,6,7,8,9,10 -a 1,2,3,4,5,6,7,8,9,10'
		print args
		time_string = st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
		print time_string
		subprocess.call(args)		

