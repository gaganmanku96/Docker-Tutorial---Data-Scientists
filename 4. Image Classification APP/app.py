import os
# os.environ['KERAS_BACKEND'] = 'plaidml.keras.backend'

import pickle

from flask import Flask, request
from PIL import Image
import numpy as np


model = None
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def classify_image():
    label = None
    try:
        f = request.files['file']
        img = Image.open(f).convert('L')
        img = np.array(img.resize((28, 28), Image.ANTIALIAS))
        img = img.reshape(1,img.shape[0], img.shape[1], 1)
        label = str(np.argmax(model.predict(img)))
    except Exception as e:
        print(str(e))
    return label


if __name__ == '__main__':
    app.run(host='0.0.0.0')
