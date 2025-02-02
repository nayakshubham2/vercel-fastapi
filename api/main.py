from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load student data from the q-vercel-python.json file
def load_student_data():
    with open('q-vercel-python.json', 'r') as file:
        return json.load(file)

# Read data from the JSON file
students_marks = load_student_data()

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [students_marks.get(name, 'Not Found') for name in names]
    return jsonify({'marks': marks})

if __name__ == '__main__':
    app.run(debug=True)
