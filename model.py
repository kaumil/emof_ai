from keras.models import model_from_json
import numpy as np
import tensorflow as tf


EMOTIONS_LIST = ["Angry", "Disgust",
                     "Fear", "Happy",
                     "Sad", "Surprise",
                     "Neutral"]

with open('face_model.json', "r") as json_file:
         loaded_model_json = json_file.read()
         loaded_model = model_from_json(loaded_model_json)
      
        # load weights into the new model
loaded_model.load_weights('face_model1.h5')
graph = tf.get_default_graph()
print("Model loaded from disk")

def predict_emotion(img):
    #print("---------------",img)
    #loaded_model._make_prediction_function()  # added
    global graph  # added
    with graph.as_default():  # added
    # model.predict_proba(new_X)

        preds = loaded_model.predict(img)
    res = np.argmax(preds)
    #print(res)
    return EMOTIONS_LIST[res],res

#
# if __name__ == '__main__':
#     pass
