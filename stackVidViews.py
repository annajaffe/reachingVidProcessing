'''
stackVidViews.py takes 2 input .avi videos and stacks them one on top of another.
First, cd into the folder with the videos to be stacked.
The user should pass in 2 video filenames (side and front), which will generate
an output .avi with the same date as the input videos if the user does not
specify an output filename.
'''

from skimage.io import imsave
import sys
from moviepy.editor import VideoFileClip, clips_array
import os

# Movies are saved in the following folder: C:\Users\SabatiniLab\Desktop\CameraVids

def main():
	if len(sys.argv) > 1:
		avi_top = sys.argv[1]
		avi_bottom = sys.argv[2]
	else:
		raise RuntimeError('AVI file was not specified')
	if len(sys.argv) == 4:
		out_file = sys.argv[3]
		if not out_file.endswith('avi'):
			out_file += '.avi'
	else:
		out_file = 'stackVid_' + avi_top[-21:-11] + '.avi' # yyyy-mm-dd
	if out_file in os.listdir('.'):
		raise RuntimeError('The stacked video already exists!')

	# Load in avi files:
	clip_top = VideoFileClip(avi_top)
	clip_bottom = VideoFileClip(avi_bottom)
	w, h = clip_top.size

	# Stack videos and save:
	final_clip = clips_array([[clip_top], [clip_bottom]])
	final_clip.write_videofile(out_file, codec='png') # write as .avi

if __name__ == '__main__':
    main()
