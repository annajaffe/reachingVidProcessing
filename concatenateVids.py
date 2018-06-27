'''
concatenateVids.py takes an input .avi filename (ex. frontCam_2018-06-22-140655-0000),
takes all of the split videos from a behavioral session for a given view, and
concatenates them into one long video.
'''

import pdb
from skimage.io import imsave
import sys
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

def main():
	if len(sys.argv) > 1:
		avi_basename = sys.argv[1]
		avi_basename = avi_basename[:-16] # get everything except the time and split num
	else:
		raise RuntimeError('AVI file was not specified')
	if len(sys.argv) == 3:
		out_file = sys.argv[2]
		if not out_file.endswith('avi'):
			out_file += '.avi'
	else:
		out_file = avi_basename + '_concat.avi'

	# Get list of filenames, in order (0000, 0001, ...)
	clips = []
	splitVidNames = [filename for filename in os.listdir('.') if filename.startswith(avi_basename)]

	print('Concatenating videos: \n' + "\n".join(str(x) for x in splitVidNames))

	for clip in splitVidNames:
		clips.append(VideoFileClip(clip))

	# Concatenate clips to make final video
	video = concatenate_videoclips(clips, method='chain')
	video.write_videofile(out_file, codec='rawvideo')
	
if __name__ == '__main__':
    main()