# coding=utf-8

import cv2
import os
import sys
import numpy as np
import re

input_path=sys.argv[1]

# 每隔多少帧取一帧
frame_interval=int(sys.argv[2])

filenames=os.listdir(input_path)

video_prefix=input_path.split(u'//')[-1]

frame_path='{}_frames'.format(input_path)


if not os.path.exists(frame_path):
    os.mkdir(frame_path)

cap=cv2.VideoCapture()

for filename in filenames:
    filepath=os.sep.join([input_path,filename])
    cap.open(filepath)

    # 总共的帧数
    n_frames=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    for i in range(42):
        cap.read()

    # print(n_frames)
    # print('{}'.format(video_prefix))
    # print(filename.split('.')[0])

    for i in range(n_frames):
        ret,frame=cap.read()

        if i % frame_interval==0:
            imagename='{}_{}_{:0>6d}.jpg'.format(video_prefix,filename.split('.')[0],i)
            imagepath=os.sep.join([frame_path,imagename])
            print('exported{}!'.format(imagepath))
            cv2.imwrite(imagepath,frame)

cap.release()
