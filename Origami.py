"""
Created on Thu Nov 15 21:29:33 2018

@author: manuel
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns


np.random.seed(2)

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import itertools

from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from keras.optimizers import RMSprop
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ReduceLROnPlateau
#input Height and Width of desired testing image
H = 28
W = 28
#recheck the pathing here
#need to put in images here
#DATA PRE-PROCESSING
#taking data with 
birdbase = pd.read_csv("Annotations/birdbase_labels.csv")
Origamicrane = pd.read_csv("Annotations/origamicrane_labels.csv")

sns.set(style='white',context='notebook',palette='deep')
#check that our information is indeed correct
bird.head()

#Grayscale images, we are searching for creases, sharp lighting differences.

#Background removal?

#DATA PROCESSING
#CNN here



#ANN here


