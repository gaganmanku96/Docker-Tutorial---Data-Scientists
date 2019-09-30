from flask import Flask, request

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def print_square():
    recieved_value = int(request.get_json(force=True))
    print(recieved_value)
    return str(recieved_value**2)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
