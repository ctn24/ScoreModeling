# Importamos las librerias
import os
import numpy as np
import glob
import shutil
import pandas as pd
import matplotlib
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Cargamos la informacion

df = pd.read_csv(os.path.normpath('C:/Users/ctn24/PycharmProjects/ScoreModeling/PML_FPS_id.csv'), index_col=None)
#df.info()
print(df.groupby('match_id'))
#
# model = Sequential()
#
# model.add(Conv2D(16, 3, padding='same', activation='relu', input_shape=(IMG_SHAPE,IMG_SHAPE, 3)))
# model.add(MaxPooling2D(pool_size=(2, 2)))
#
# model.add(Conv2D(32, 3, padding='same', activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
#
# model.add(Conv2D(64, 3, padding='same', activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
#
# model.add(Flatten())
# model.add(Dropout(0.2))
# model.add(Dense(512, activation='relu'))
#
# model.add(Dropout(0.2))
# model.add(Dense(5))

















