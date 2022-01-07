import requests
import json
from tensorflow.keras.models import model_from_json


def get_model():
    ''' Returns Model loaded with original weights'''
    url='https://download1505.mediafire.com/cmfy86beuiug/4dzzr51rq7ix2cy/var600_model3.json'
    file=requests.get(url)
    model_arch=json.dumps(file.json())
    model=model_from_json(model_arch)
    model.load_weights('weights.h5')
    return model