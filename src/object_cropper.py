import os
import numpy as np
import skimage
import matplotlib
import matplotlib.pyplot as plt
import cv2
import pickle
import math
import scipy.interpolate
from scipy.ndimage import gaussian_filter
from skimage import color
from matplotlib.colors import LightSource
from mpl_toolkits.mplot3d import Axes3D
from pylab import cm
from mpl_toolkits.mplot3d import proj3d

def imread(name):
    res = cv2.imread(name)
    res = res[...,::-1] # BGR to RGB
    return res

def imwrite(name, data):
    cv2.imwrite(name, data[:, :, ::-1])

SRC_IMAGE = "../data/bottle/image3.jpg"
OUT_DIR = "../data/bottle/bottle_mask.pickle"
image = imread(SRC_IMAGE)

_, ax = plt.subplots()

ax.imshow(image)
pts = matplotlib.pyplot.ginput(n=-1, timeout=-1)

ax.add_patch(matplotlib.patches.Polygon(pts, fill=False, color='white', linewidth=0.2))
with open(OUT_DIR, 'wb') as handle:
    pickle.dump(pts, handle)
