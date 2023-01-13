import cv2
import numpy as np
import glob

FPS = 3
resize = 1000
root = '/media/khw/T7/Humandataset/MPI/mpi_inf_3dhp/mpi_inf_3dhp_test_set/TS6/imageSequence'
# root = '/media/khw/Samsung_T5/0703/H36M4/experiments/eval_trainset_S8'

video_name = '3DHP_TS6.avi'
# video_name = './H36M/h36m_S8_1.avi'

# root = '/media/khw/Samsung_T5/0703/H36M4/experiments/H36M_baseline/h36m8_hp_img_joints/plot3D'
# video_name = 'H36M_S8_plot3D_baseline.avi'

img_files = sorted(glob.glob(root +'/*.jpg'))

img_files = img_files[106:]

img_array = []
for filename in img_files:
    img = cv2.imread(filename)
    # img = cv2.resize(img, (resize, resize))
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
 
out = cv2.VideoWriter(video_name,cv2.VideoWriter_fourcc(*'DIVX'), FPS, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()