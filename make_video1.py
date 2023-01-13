import os
import argparse

import cv2
import numpy as np
from glob import glob
import shutil
folder = '/media/khw/T7/Humandataset/MPI/3DHP/TS5'
filename_extension = 'jpg'
parser = argparse.ArgumentParser(description="tracking demo")

parser.add_argument('--img_set_folder', default=folder, type=str,
                    help='videos or image files')
parser.add_argument('--filename_extension', default=filename_extension, type=str,
                    help='filename_extension')
parser.add_argument('--show', default=False, type=bool,
                    help='filename_extension')
args = parser.parse_args()
root=args.img_set_folder
fexten=args.filename_extension 
shows=args.show 

print(root)

pathOutput = '3DHP_TS5_1.mp4'
fps = 15

def get_frames(video_name):
    images = glob(os.path.join(video_name, '*.'+fexten))
    images = sorted(images, key=lambda x: x.split('/')[-1].split('.')[0])
        # key=lambda x: int(x.split('/')[-1].split('.')[0]))
    for img in images:
        frame = cv2.imread(img)
        yield frame

def main():
    name = root.split('/')[-1].split('.')[0]
    frame_array = []
    for frame in get_frames(root):
        height, width, layers = frame.shape 
        size = (width, height)
        frame_array.append(frame)

        if shows:
            # image resize
            cv2.namedWindow(name, cv2.WINDOW_NORMAL)
            cv2.resizeWindow(name, 480, 640)
            # image show
            cv2.imshow(name, frame)
            cv2.waitKey(40)

    out = cv2.VideoWriter(pathOutput, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()

if __name__=="__main__":
    main()

