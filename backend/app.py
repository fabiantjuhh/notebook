from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/data")
def get_data():
    df = pd.DataFrame({
        "Name": ["Alpha", "Beta", "Charlie"],
        "Zone": ["25AD", "30AD", "35AD"]
    })
    return df.to_dict(orient="records")