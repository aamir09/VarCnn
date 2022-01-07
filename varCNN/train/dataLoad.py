import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def load_data(path,input_shape=(256,256)):
    '''The function uses ImageDataGenerator with flow_from directory to generate train and validation data 
       path: destination path for the folder where the data resides
       input_shape: determine the target shape of the images
       Returns traingen(train data) and valgen(validation data)
    '''
    datagen=ImageDataGenerator(rescale=1./255,validation_split=0.2,brightness_range=[1.2,2],horizontal_flip=True,vertical_flip=True,rotation_range=90)
    traingen=datagen.flow_from_directory(path,batch_size=32,class_mode='binary',subset='training',target_size=input_shape)
    valgen=datagen.flow_from_directory(path,batch_size=32,class_mode='binary',subset='validation',target_size=input_shape)
    return (traingen,valgen)