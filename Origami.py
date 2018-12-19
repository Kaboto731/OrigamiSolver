"""
Created on Thu Nov 15 21:29:33 2018

@author: manuel
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import imageio
import skimage
import skimage.io
import skimage.transform
import numpy as np
import scipy

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
H = 100
W = 100
#recheck the pathing here
#need to put in images here
#DATA PRE-PROCESSING
#taking data with 
base_train = pd.read_csv("Annotations/base_labels.csv")
base_test  = pd.read_csv("Annotations/Finished_labels.csv")
sns.set(style='white',context='notebook',palette='deep')
#check that our information is indeed correct
base_train.head()
#General Error catching for images along with formatting
def readskip(file):
  try:
    img = skimage.io.imread(img_folder+file)
    img = skimage.transform.resize(img, (img_width, img_height),mode = 'reflect')
    return img[:,:,:img_channels]
  except:
    return None
  #Applying our function to the csv files
base_train['img']=base_train['filename'].apply(readskip)
base_test['img'] = base_test['filename'].apply(readskip)
base_train.dropna(inplace = True)
base_test.dropna(inplace = True)

#generating more images:
generator = ImageDataGenerator(
        featurewise_center = False,
        samplewise_center = False,
        featurewise_std_normalization = False,
        zca_whitening = False,
        rotation_image = 180,
        zoom_range = 0.1,
        width__shift_range = 0.1,
        horizontal_flip = True,
        vertical_flip = True)
generator.fit(base_train)

#Splitting our original base_train to have a validation step
base_train, base_val = train_test_split(base_train, test_size = 0.1, random_state=24)
#Grayscale images, we are searching for creases, sharp lighting differences?

#Background removal?




#CNN built here
model = Sequential()
#since we are grayscaling our images R=G=B our imageshape now only contains a dimension of 1
model.add(Conv2D(6, kernel_size = 3,input_shape(img_width, img_height,1), activation = 'relu'))
model.add(MaxPool2D(2))
model.add(Conv2D(12, kernel_size =3, activation = 'relu'))
model.add(Flatten())
model.add(Dense(train_labels.columns.size, activation = 'softmax'))
model.compile(optimizer = 'rmsprop', loss = 'categorical_crossentropy', metrics = ['accuracy'])
#A stopping condition for if we are not actually improving our results within 10 epochs
earlystopper =EarlyStopping(monitor = 'val_loss', patience = 10, verbose =1)
greatmod= ModelCheckpoint('best_model.h5', mointor='val_loss', verbose=1, save_best_only=True, save_weights_only=True)



#ANN here


