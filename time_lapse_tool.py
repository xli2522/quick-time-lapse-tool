                ###        © Xiyuan Li 2021       ###
                ###        xli2522 @ github       ###
                ###     Quick Time-lapse Tool     ###
                ###  *Image to video with openCV  ###

import cv2
import numpy as np
import datetime
import os.path, time
import glob
import io
import shutil

def main():
    '''Main'''
    timelapse('demo.mp4', 10, r"C:\Users\Documents\GitHub\timelapsetool\test_image")     # folder address of your own
   
    return 

def timelapse(title, fps, folder_path, inspect = True):
    '''Function constructs time-lapse video from images in a folder.
        Inputs:      title   (string)     video title + .mp4/other common video format
                     fps     (double)     time-lapse video frames per second 
                     folder_path    (raw string)    location of the image folder
                     inspect    (boolean)       True (default)/False
        Output:
                     time-lapse video 

        **folder_path example:
                r"/your/address/PythonProjects/time-lapse/images"
                *r indicates raw string
        '''

    #* Image Processing
    imgFolder = folder_path     # folder loation 
    cvImages = []     # image container for opencv
    img_entries = (os.path.join(imgFolder, file_name) for file_name in os.listdir(imgFolder))       # access all images in the directory
    img_entries = list(img_entries)         # type generator ==> list
    img_entries.sort(key=os.path.getatime)      # sort files ==> creation time
    num = len(img_entries)       # number of files collected

    for image in img_entries:       # read all sorted images 
        cvIm = cv2.imread(str(image))       
        if cvIm is not None:    
            cvImages.append(cvIm)       # add images to opencv image container

    frame_spec = cvImages[0]        # sample the first image in the container
    height, width, layers = frame_spec.shape        # get image specs

    #* Video Construction
    fourcc = cv2.VideoWriter_fourcc(*'XVID')        # set video specs
    video = cv2.VideoWriter(title, fourcc, fps, (width, height))  # create opencv video object

    for frame in cvImages:          # access each frame in the image container
        video.write(frame)         # write frame

        if inspect:         # if True, show frame
            cv2.imshow('Inspection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):       # stop the process when interupted by key q
            break 

    cv2.destroyAllWindows()     # destroy any open window
    video.release()            # release the video

    return 

main()      # run main