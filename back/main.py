from flask import Flask, jsonify
from multiprocessing import freeze_support
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    print('sdfsdfsdfsfsdf')
    return jsonify('Main from Python')

if __name__ == '__main__':
    app.run(debug=True, port=5174)