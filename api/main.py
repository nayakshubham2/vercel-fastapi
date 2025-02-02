from fastapi import FastAPI
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

@app.get("/api")
async def read_names(name: str = None):  # type: ignore
    if name:
        names = name.split("&name=") # split string by &name=
        return {"names": names}
    return {"message": "No names provided"}



@app.get("/")
async def get_default():
    return "Hello World!"
