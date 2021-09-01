from logging import debug
from flask import Flask
from flask.json import jsonify

app = Flask(__name__)

@app.route('/home')
def main():
    return jsonify({'hello':'world'}), 200

app.run(debug=False)