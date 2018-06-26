'''
This script converts an avi movie into an h5 dataset under the dataset name /box
for use with the LEAP preprocessing framework
'''
import sys
import h5py
import numpy as np
from moviepy.editor import VideoFileClip
import os

def main():
  if len(sys.argv) > 1:
    avi_file = sys.argv[1]
  else:
    raise RuntimeError('AVI movie file was not specified!')
  if len(sys.argv) == 3:
    out_file = sys.argv[2]
    if not out_file.endswith('h5'):
      out_file += '.h5'
  else:
    out_file = 'processed.h5'

  # Set up path for saving the output .h5
  baseFolder = baseFolder = r'C:\Users\SabatiniLab\Documents\GitHub\leap\videosAsH5'
  if not os.path.exists(baseFolder):
    os.makedirs(baseFolder)
  savePath = os.path.join(baseFolder, out_file)

  # load in avi file
  clip = VideoFileClip(avi_file)
  w, h = clip.size

  f = h5py.File(savePath, 'w')
  # create the box dataset
  dataset = f.create_dataset('box', shape=(1, 1, *clip.size), dtype='u1', maxshape=(None, 1, *clip.size))

  # loop through each frame
  for i, frame in enumerate(clip.iter_frames(dtype='u1', progress_bar=True)):
    # add space for the next frame
    dataset.resize(i+1, axis=0)
    # swap dims
    frame = np.swapaxes(frame, 0, 1)
    # save only one color into the dataset
    dataset[i, 0, :, :] = frame[:, :, 0]


if __name__ == '__main__':
  main()
