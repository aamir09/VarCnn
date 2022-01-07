import numpy as np 
import pandas as pd 
import tensorflow as tf


def create_model(input_shape=(256,256)):
    '''input_shape: Shape of the input the CNN would take
       Returns Tensorflow Model Object'''

#NN From Scracth 


    inputs=tf.keras.Input(input_shape)
    #Initial Layers of 256 Filters 
    x=tf.keras.layers.Conv2D(64,5,padding='same')(inputs)
    x=tf.keras.layers.Activation(activation='relu')(x)
    x=tf.keras.layers.MaxPool2D(strides=(2,2))(x)
    x=tf.keras.layers.Conv2D(64,5,padding='same')(inputs)
    x=tf.keras.layers.Activation(activation='relu')(x)
    x=tf.keras.layers.MaxPool2D(strides=(2,2))(x)
    x=tf.keras.layers.Conv2D(64,5,padding='same')(x)
    x=tf.keras.layers.Activation(activation='relu')(x)
    x=tf.keras.layers.MaxPool2D(strides=(2,2))(x)
    x=tf.keras.layers.Conv2D(64,5,padding='same')(x)
    x=tf.keras.layers.Activation(activation='relu')(x)
    x=tf.keras.layers.MaxPool2D(strides=(2,2))(x)



    #Decreasing Filters and MAxPool Layers
    x=tf.keras.layers.Conv2D(32,3,padding='same',dilation_rate=2)(x)
    x=tf.keras.layers.Activation(activation='relu')(x)
    # x=tf.keras.layers.BatchNormalization()(x)
    x=tf.keras.layers.MaxPool2D(strides=(2,2))(x)
    x=tf.keras.layers.Conv2D(16,3,padding='same',dilation_rate=2)(x)
    x=tf.keras.layers.Activation(activation='relu')(x)
    x=tf.keras.layers.MaxPool2D(strides=(2,2))(x)
    # x=tf.keras.layers.BatchNormalization()(x)
    x=tf.keras.layers.Conv2D(16,3,padding='same',dilation_rate=2)(x)
    x=tf.keras.layers.Activation(activation='relu')(x)
    x=tf.keras.layers.MaxPool2D(strides=(2,2))(x)
    # x=tf.keras.layers.BatchNormalization()(x)

    #Dense Layers 
    x=tf.keras.layers.GlobalAveragePooling2D()(x)
    x=tf.keras.layers.Dense(400,kernel_regularizer='l1')(x)
    x=tf.keras.layers.Activation(activation='relu')(x)
    x=tf.keras.layers.Dense(512,kernel_regularizer='l1')(x)
    x=tf.keras.layers.Dropout(0.5)(x)
    x=tf.keras.layers.Activation(activation='relu')(x)
    x=tf.keras.layers.Dense(400,kernel_regularizer='l1')(x)
    x=tf.keras.layers.Dropout(0.5)(x)
    x=tf.keras.layers.Activation(activation='relu')(x)
    x=tf.keras.layers.Dense(1)(x)
    #Output
    out=tf.keras.layers.Activation(activation='sigmoid')(x)

    model=tf.keras.Model(inputs,out,name='BaseModel')

    return model


       



    


    

