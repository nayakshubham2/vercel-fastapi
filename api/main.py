from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Sample marks data for 100 students
student_data = [{"name":"h0c0F3t","marks":38},{"name":"kC6cO","marks":82},{"name":"T","marks":44},{"name":"t","marks":73},{"name":"YhnbEW3","marks":65},{"name":"9kJ8yT","marks":61},{"name":"xpg","marks":69},{"name":"iOe3GYnjd","marks":79},{"name":"BVSL","marks":47},{"name":"CT00qo2","marks":27},{"name":"VB69t","marks":13},{"name":"m","marks":20},{"name":"tATfPQAR","marks":37},{"name":"vrpLHvV","marks":46},{"name":"B","marks":59},{"name":"qMrp","marks":42},{"name":"7HZhr5Z","marks":82},{"name":"jylGr","marks":84},{"name":"UiwzGhcJ2p","marks":10},{"name":"bwRSJK","marks":19},{"name":"dqrbz","marks":29},{"name":"Qs","marks":2},{"name":"How3ZFwSzl","marks":36},{"name":"ZQw","marks":43},{"name":"4Ng","marks":97},{"name":"eu6ds6","marks":30},{"name":"OuG","marks":24},{"name":"svxQE","marks":79},{"name":"Jwzp","marks":18},{"name":"DeOhh4","marks":81},{"name":"6vtO9Ks","marks":66},{"name":"km","marks":73},{"name":"cMBX","marks":14},{"name":"Mt2DKi","marks":72},{"name":"QbR1Y","marks":19},{"name":"2DNC","marks":62},{"name":"JZgeL5AyOB","marks":85},{"name":"Zem1bm","marks":95},{"name":"kE9tUeAGZ","marks":46},{"name":"q5f","marks":58},{"name":"KKwJr","marks":26},{"name":"XhbW","marks":51},{"name":"j","marks":97},{"name":"Ho0","marks":83},{"name":"9ofokwRZ","marks":52},{"name":"KODUAk","marks":75},{"name":"JV84VenKi","marks":12},{"name":"4ZIT9xMB","marks":52},{"name":"2G3ow","marks":37},{"name":"MOjMoaEPb0","marks":86},{"name":"5","marks":88},{"name":"8hx","marks":48},{"name":"PCsFX2e822","marks":18},{"name":"b6pos7","marks":40},{"name":"5GuOw","marks":9},{"name":"fvpxosY","marks":91},{"name":"WDoyk1Az","marks":61},{"name":"P5CzD","marks":52},{"name":"310dytyJV7","marks":79},{"name":"hPn3Yu4","marks":28},{"name":"vT","marks":84},{"name":"I5","marks":38},{"name":"q6","marks":0},{"name":"mnZOVdCed","marks":28},{"name":"emHSO9","marks":39},{"name":"3BmwRR4Yn","marks":18},{"name":"2Rs6YOmBv","marks":7},{"name":"4BB9","marks":42},{"name":"ZcUgr","marks":75},{"name":"pZguqMd71N","marks":54},{"name":"cDGHfs","marks":33},{"name":"JmIOzFk9oj","marks":91},{"name":"ag","marks":2},{"name":"J6HceOc6K","marks":75},{"name":"JlQY4Z6","marks":89},{"name":"MPO9H","marks":3},{"name":"BFqMK","marks":49},{"name":"U9CEzjtbN","marks":83},{"name":"W88aPso8","marks":8},{"name":"3hLzd4oo","marks":30},{"name":"mI4RZ","marks":87},{"name":"BHVx","marks":90},{"name":"4Xeqc76","marks":69},{"name":"X","marks":28},{"name":"vJ96GZEVDp","marks":8},{"name":"EYIO","marks":87},{"name":"2AM323yW8g","marks":44},{"name":"jJysPqPY","marks":17},{"name":"nKLqlFn0","marks":78},{"name":"AJdRpIL","marks":58},{"name":"W","marks":82},{"name":"7nCJ","marks":41},{"name":"AV4XNRS","marks":10},{"name":"9tC3xhS2lR","marks":63},{"name":"8ml","marks":42},{"name":"mK","marks":7},{"name":"nnMRd5x","marks":38},{"name":"3Teenqiic","marks":30},{"name":"wJ","marks":89},{"name":"QVzE","marks":10}]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


# Create a dictionary for faster lookup (name -> marks)
student_marks = {}
for student in student_data:
    student_marks[student["name"]] = student["marks"]


@app.get("/api")
async def get_marks(name: str = None):
    if name is None:
        return {"message": "No names provided"}

    names = name.split("name=") # Split by &name= to get list of names
    marks = []
    not_found = []
    for student_name in names:
        mark = student_marks.get(student_name.strip('?'))
        if mark is not None:
            marks.append(mark)
        else:
            not_found.append(student_name)

    if not_found:
        return {"message": f"Marks not found for: {', '.join(not_found)}"}

    return {"marks": marks,"not_found": names}
