# import pdb
from skimage.io import imsave
import os # added AJ
import h5py
import sys


def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        raise Exception('Please provide an h5 filename')
    new_fname = input_file[:-3] + '-image-{:08d}.png'

    # added AJ:
    baseFolder = r'C:\Users\SabatiniLab\Documents\GitHub\leap' # need to put r in front for "raw string"
    savePath = os.path.join(baseFolder, input_file[:-3])
    if not os.path.exists(savePath):
        os.makedirs(savePath)
    #

    f = h5py.File(input_file, 'r')
    for i, frame in enumerate(f['box']):
        new_fname_path = os.path.join(savePath, new_fname.format(i)) # save images into new folder
        imsave(new_fname_path, frame[0].T) # transpose images so they're in original recorded format

# pdb.set_trace()

if __name__ == '__main__':
    main()
