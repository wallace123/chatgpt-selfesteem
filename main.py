import os
from flask_cors import CORS
from flask import Flask, request, jsonify, send_from_directory


app = Flask(__name__)
CORS(app)

well_known_dir = os.path.join(app.root_path, '.well-known')

@app.route('/.well-known/<path:filename>')
def well_known(filename):
    return send_from_directory(well_known_dir, filename)

@app.route('/run', methods=['GET'])
def run_command():
    output = """
You are an expert therapist that provides summaries on daily sef esteem sentence
completions. I will provide what I wrote and you will summarize it."""

    return jsonify(output)

if __name__ == '__main__':
    app.run(host='localhost', port=1234)