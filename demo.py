                ###        © Xiyuan Li 2021       ###
                ###        xli2522 @ github       ###
                ###      Time-lapse Tool Demo     ###
                ###  *Image to video with openCV  ###

####################################
###### Use time_lapse_tool.py ######
####################################
from time_lapse_tool import *

timelapse('demo.avi', 10, r"C:\Users\xli2522\Documents\GitHub\test_image")      # change folder address to your own

#################################
###### Use plt_to_video.py ######
#################################
import matplotlib.pyplot as plt
from plt_to_video import *

# waht your matplotlib loop might look like
def test_matplot_loop(n):
    '''This function tests the function
        Input:      n   number of frames
    '''
    images = []     # empty image container
    plt.figure()    # initialize matplotlib figure
    for i in range(n):
        plt.plot([np.random.randint(2), np.random.randint(2)])      # generate random plots for demo
        plt.title("test" + str(i))
        images = savebuff(plt, images)      # save image in in-memory location
        plt.clf()
    
    construct(images, 'matplot_demo.avi', 5)        # construct video; 5 fps

    return 

test_matplot_loop(100)      # construct a demo video with 100 frames