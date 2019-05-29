
from __future__ import print_function
#General
import pandas as pd
import numpy as np
import math, random, warnings, colorsys, fitsio, scipy, os, glob, json, re
from sklearn.neighbors import KernelDensity
from itertools import product

#Astronomy
import astropy
from astropy.io import fits
#import pyfits
from astropy import wcs
from astropy.utils.data import get_pkg_data_filename
from astropy.coordinates import SkyCoord, ICRS  # High-level coordinates 
import astropy.units as u

#Graphics
from PIL import Image
from matplotlib.pyplot import imshow
import seaborn as sns
import matplotlib as mpl
from matplotlib import pyplot
import matplotlib.pyplot as plt
import cv2
import pickle
from scipy.ndimage.filters import gaussian_filter
from scipy.interpolate import interp1d
from scipy.ndimage.filters import maximum_filter, minimum_filter, convolve

#DL
from keras.preprocessing.image import ImageDataGenerator
#import skimage.io as io
#import skimage.transform as trans
from keras.models import *
from keras.layers import *
from keras.layers import BatchNormalization, Activation
from keras.optimizers import *
from keras.callbacks import ModelCheckpoint, LearningRateScheduler, ProgbarLogger, TensorBoard,LambdaCallback, Callback
from keras import losses
from keras import backend as keras
from functools import partial,update_wrapper


from notebook.services.config import ConfigManager
from tqdm import tqdm_notebook
import importlib
import erospy, shutil, itertools
