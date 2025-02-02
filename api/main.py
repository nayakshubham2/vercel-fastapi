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
async def get_marks(name: Optional[list[str]] = None):
    if name is None:
        return {"message": "No names provided"}
    return {"received_names": name}


@app.get("/")
async def get_default():
    return "Hello World!"
