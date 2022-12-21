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

with open(f"../output/bottle2/heights.pickle", 'rb') as handle:
    heights = pickle.load(handle)

def plot_surface(name, Z, height, angle):
    # Z is an HxW array of surface depths
    H, W = Z.shape
    x, y = np.meshgrid(np.arange(0,W), np.arange(0,H))
    # set 3D figure
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # add a light and shade to the axis for visual effect
    # (use the ‘-’ sign since our Z-axis points down)
    ls = LightSource()
    color_shade = ls.shade(-Z, plt.cm.gray)
    # display a surface
    # (control surface resolution using rstride and cstride)
    surf = ax.plot_surface(x, y, -Z, facecolors=color_shade, rstride=4, cstride=4)
    ax.view_init(elev=height, azim=angle)
    # turn off axis
    plt.axis('off')
    if name is not None:
        plt.savefig(name, bbox_inches='tight')
    plt.show()

plot_surface(None, heights, 40, 50)