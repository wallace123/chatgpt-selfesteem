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
You are an expert therapist. I am working on daily sentence completions to improve self esteem. 
The exercises come from an appendix from the book The Six Pillars of Self-Esteem by Nathaiel Branden.
When I provide you with my input from the week, I need you to provide 5 completions to the following,
-	If any of what I wrote this week is true, it might be helpful if I –.
I then want you to provide advice on how I can implement your suggestions."""

    return jsonify(output)

if __name__ == '__main__':
    app.run(host='localhost', port=1234)