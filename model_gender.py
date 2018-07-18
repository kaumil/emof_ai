from keras.models import model_from_json
import numpy as np
import tensorflow as tf


GEN_LIST = ["female", "male"]

with open('models/gender_model_imdb_gpu.json', "r") as json_file:
         loaded_model_json = json_file.read()
         loaded_model = model_from_json(loaded_model_json)

        # load weights into the new model
loaded_model.load_weights('models/gender_model_imdb_gpu.h5')
graph = tf.get_default_graph()
print("Model loaded from disk")
loaded_model.summary()

def predict_gender(img):
    global graph
    #graph = tf.get_default_graph()  # added
    with graph.as_default():
        preds = loaded_model.predict(img)
    res = np.argmax(preds)
    return GEN_LIST[res], res



if __name__ == '__main__':
    pass