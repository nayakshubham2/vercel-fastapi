from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json
from pathlib import Path

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load and preprocess marks from JSON file
MARKS_FILE = Path(__file__).parent / "q-vercel-python.json"
with open(MARKS_FILE) as f:
    marks_list = json.load(f)
    marks_db = {entry["name"]: entry["marks"] for entry in marks_list}

@app.get("/")
async def root():
    return JSONResponse(content={"marks": marks_db})

@app.get("/api")
async def marks(request: Request):
    names = request.query_params.getlist("name")
    result = [marks_db.get(name, 0) for name in names]
    return JSONResponse(content={"marks": result})
