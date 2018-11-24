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
#need to put in images here
train = pd.read_csv("../Origamiimg/BirdBase/birdbaseimgs.csv")
#validation
Vali1_1 = pd.read_csv("../Origamiimg/Crane/Crane.csv")
Vali2_1 = pd.read_csv("../Origamiimg/Crane2/Crane2.csv")
                    
#base comparison with things not built in the system
test1_0 = pd.read_csv("../Origamiimg/WaterbombBase/waterbombbase.csv")


#K-fold cross validation might be needed to show which bases hold better approx.
#be prepared to have long computation times with this ^

sns.set(style='white',context='notebook',palette='deep')
