'''
stackVidViews.py takes 2 input .avi videos and stacks them one on top of another.
First, cd into the folder with the videos to be stacked.
The user should pass in the side view first (top), the front view (bottom),
and then the output filename.
E.g., python stackVidViews.py sideCam.avi frontCam.avi combined.avi
'''

from skimage.io import imsave
import sys
from moviepy.editor import VideoFileClip, clips_array

# Movies are saved in the following folder: C:\Users\SabatiniLab\Desktop\CameraVids

def main():
	if len(sys.argv) > 1:
		avi_side = sys.argv[1]
		avi_front = sys.argv[2]
	else:
		raise RuntimeError('AVI file was not specified')
	if len(sys.argv) == 4:
		out_file = sys.argv[3]
		if not out_file.endswith('avi'):
			out_file += '.avi'
	else:
		out_file = 'concatVid.avi'

	# Load in side and front avi files:
	clip_side = VideoFileClip(avi_side)
	clip_front = VideoFileClip(avi_front)
	w, h = clip_side.size

	# Stack videos and save:
	final_clip = clips_array([[clip_side], [clip_front]])
	final_clip.write_videofile(out_file, codec='rawvideo') # write as .avi

if __name__ == '__main__':
    main()
