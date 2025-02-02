from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# Sample marks data for 100 students
student_marks = {
    "X": 10,
    "Y": 20,
    # Add other student names and marks up to 100
}

@app.get("/api")
async def get_marks(name: list[str]):
    marks = [student_marks.get(n, "Not Found") for n in name]
    return JSONResponse(content={"marks": marks})
