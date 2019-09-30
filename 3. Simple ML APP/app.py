import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)


model = None
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/predict', methods=['POST'])
def predict():
    parameters = request.get_json(force=True)
    features = str(parameters).split('-')
    f1, f2, f3 = int(features[0]), int(features[1]), int(features[2])
    spending_score = model.predict(([f1, f2, f3],))[0]
    return jsonify(spending_score)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
