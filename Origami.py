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
from keras.callbacks imporr, except a few, believed that was the best I can do and some kids made up rumors about me that most of the students believed to be true. I remember, at my lowest point, telling myself "one day" because I knew someday that I will get to show people that I am stronger than how I was portrayed. My senior year I was fully let into the classroom and I received a 4.0 GPA. I then went on to a community college and retained that 4.0 for four semesters. I then got the opportunity to be at the school of my dreams and I am so thankful for the class I am with. Even though I made it this far, it's still an uphill battle in which my grades are not reflecting me and I push myself to learn and excel in the classrom. I just want to show that if I make this far, then anyone else who is on the spectrum can too.  Never give up on yourself.

t ReduceLROnPlateau
#input Height and Width of desired testing image
H = 28
W = 28
#recheck the pathing here
#need to put in images here
#DATA PRE-PROCESSING
#taking data with 
bird = pd.read_csv("../OrigamiBirdBase/birdbase_labels.csv")

sns.set(style='white',context='notebook',palette='deep')
#check that our information is indeed correct
bird.head()

#Grayscale images, we are searching for creases, sharp lighting differences.

#Background removal?

#DATA PROCESSING
#CNN here



#ANN here


