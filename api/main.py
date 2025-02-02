from fastapi import FastAPI
from typing import List, Optional
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Sample marks data for 100 students
student_marks = {
    "X": 10,
    "Y": 20,
    # Add other student names and marks up to 100
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

try:
    with open("q-vercel-python.json", "r") as f:
        student_marks = json.load(f)
except FileNotFoundError:
    student_marks = {}

@app.get("/api")
async def read_names(name: str = None):  # type: ignore
    marks = []
    not_found = []
    for student_name in name:
        mark = student_marks.get(student_name)
        if mark is not None:
            marks.append(mark)
        else:
            not_found.append(student_name)

    if not_found:
      return {"message": f"Marks not found for: {', '.join(not_found)}"}
    
    return {"marks": marks}



@app.get("/")
async def get_default():
    return "Hello World!"
