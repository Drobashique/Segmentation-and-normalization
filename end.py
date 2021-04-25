from PIL import Image
import skimage
from skimage import data, io, filters,morphology,segmentation,feature
from scipy import ndimage
from skimage import color
import numpy as np
import math
import sys, getopt

for i in range(1,11):
    im1 = Image.open("/Users/vladimirlisovoi/desktop/учеба/diplom/quad/out{0}.png".format(i))
    data1 = np.array(im1)
    fd1 = data1.astype(np.float)

    im = Image.open("/Users/vladimirlisovoi/desktop/учеба/diplom/quad/s1_test_{0}.png".format(i))
    data = np.array(im)
    fd = data.astype(np.float)
    print(fd.shape[0],fd.shape[1],fd1.shape[0],fd1.shape[1])
    newobj = np.zeros((fd.shape[0]+1,fd.shape[1]+1,3))
    for k in range(fd1.shape[0]):
        for j in range(fd1.shape[1]):
            if fd1[k][j] == 255:
                newobj[k][j] = fd[k][j]
                #print(fd1[i][j])
            else:
                newobj[k][j] = 255
    newobj = newobj.astype(np.uint8) 
    omg = Image.fromarray(newobj)
    omg.show()
    omg.save("/Users/vladimirlisovoi/desktop/учеба/diplom/quad/an_res_{0}.png".format(i))
