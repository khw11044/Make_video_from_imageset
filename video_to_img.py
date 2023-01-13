import cv2
vfile = '/media/khw/T7/Humandataset/MPI/mpi_inf_3dhp/mpi_inf_3dhp_test_set/TS6/3DHP_T6.mp4'
save_root = '/media/khw/T7/Humandataset/MPI/mpi_inf_3dhp/mpi_inf_3dhp_test_set/TS6/imageSequence'
vidcap = cv2.VideoCapture(vfile)
success,image = vidcap.read()
count = 1
while success:
  cv2.imwrite(save_root + "/%06d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

print("finish! convert video to frame")