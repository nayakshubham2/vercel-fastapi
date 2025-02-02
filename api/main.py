from fastapi import FastAPI
import json

app = FastAPI()

# Load student data from the q-vercel-python.json file
def load_student_data():
    with open('q-vercel-python.json', 'r') as file:
        return json.load(file)

# Read data from the JSON file
students_marks = load_student_data()

@app.get('/api')
async def get_marks(name: List[str]):
    marks = [students_marks.get(name, 'Not Found') for name in names]
    return jsonify({'marks': marks})
