from keras.models import model_from_json
import numpy as np


import tensorflow as tf
AGE_LIST = ["adult", "child",
                     "old", "youth"]

with open('models/model_age_IMDB_gpu.json', "r") as json_file:
         loaded_model_json1 = json_file.read()
         loaded_model1 = model_from_json(loaded_model_json1)

        # load weights into the new model
loaded_model1.load_weights('models/model_age_IMDB_gpu.h5')
graph = tf.get_default_graph()
print("Model loaded from disk")

def predict_age(img):
    #model._make_prediction_function()  # added
    global graph
    #graph = tf.get_default_graph()  # added
    with graph.as_default():  # added
        #model.predict_proba(new_X)
    #print('---------------',loaded_model_json)
    #print('+++++++++++++++',loaded_model)
        preds = loaded_model1.predict(img)
    res = np.argmax(preds)
    return AGE_LIST[res],res


# if __name__ == '__main__':
#     pass
