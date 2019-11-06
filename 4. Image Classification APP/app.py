from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
from tensorflow import keras

model = keras.models.load_model('model.h5')

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def classify_image():
    label = None
    f = request.files['file']
    print(f)
    img = Image.open(f).convert('L')
    img = np.array(img.resize((28, 28)))/255.0
    img = img.reshape(1, img.shape[0], img.shape[1], 1)
    label = int(np.argmax((model.predict(img))))
    print(label)
    return jsonify(label)


if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run()
