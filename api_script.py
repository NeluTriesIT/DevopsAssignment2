from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/api', methods = ['GET'])

def get_random_number():
    return jsonify({"number": random.randint(0,100000)})

if __name__ == '__main__':
    app.run(debug=True)