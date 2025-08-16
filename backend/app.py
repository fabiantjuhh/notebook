from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/data")
def get_data():
    df = pd.DataFrame({
        "Name": ["Alpha", "Beta", "Charlie"],
        "Zone": ["25AD", "30AD", "35AD"]
    })
    return df.to_dict(orient="records")