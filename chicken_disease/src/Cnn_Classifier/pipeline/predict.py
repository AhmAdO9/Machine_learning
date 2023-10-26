import os
import numpy as np
from keras.preprocessing import image
from keras.models import load_model


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename


    def predict(self):
        model = load_model(os.path.join("artifacts","training","model.h5"))

        imagename=self.filename
        test_image=image.load_img(imagename, target__size=(224,224))
        test_image=image.img_to_array(test_image)
        test_image=np.expand_dims(test_image, axis=0)
        result=np.argmax(model.predict(test_image),axis=1)
        print(result)

        if result[0]==1:
            prediction="Healthy"
            return [{"image": prediction}]
        else:
            prediction="Coccidiosis"
            return [{"image":prediction}]