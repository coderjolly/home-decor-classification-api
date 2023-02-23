import tensorflow as tf
from tensorflow import keras
import numpy as np

def classificationModel(path):
    
    image_size = (180, 180)
    loaded_model = tf.keras.models.load_model('model/save_at_43.h5')
    
    img = keras.preprocessing.image.load_img(path, target_size=image_size)
    
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    classes = {0: 'Bed', 1: 'Chair', 2: 'Sofa'}
    prediction = classes[np.argmax(loaded_model.predict(img_array))]

    return prediction