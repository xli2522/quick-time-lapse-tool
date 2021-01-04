                ###        © Xiyuan Li 2021       ###
                ###        xli2522 @ github       ###
                ###    Matplotlib plt to video    ###
                ###  *Image to video with openCV  ###
import cv2
import numpy as np
import os.path
import glob
import io
from PIL import Image

def savebuff(frame, container):
    '''Function saves image in in-memory location
        Inputs:     frame   (matplotlib image)  
                    container   (list)     empty image container
        Output:     container   (list)      image container with added frame location
    '''

    buf = io.BytesIO()      # create in-memory buffer location
    frame.savefig(buf, format='jpeg')       # save buffer image in jpeg format (*3 channels)
    container.append(buf)       # add the 

    return container

def construct(container, title, fps, inspect=True):
    '''Function constructs video from images in the container.
        Inputs:     container   (list)      image container with frame location
                    title   (string)     video title + .avi
                    fps     (double)     time-lapse video frames per second 
                    inspect    (boolean)       True (default)/False
        Output:
                    video
    '''
    #* Image Processing
    cvImages = []     # image container for opencv
    for image in container:       # read all sorted images 
        cvIm = np.asarray(Image.open(image))
        image.close()
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