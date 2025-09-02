from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/data")
# def get_data():
#     df = pd.DataFrame({
#         "Name": ["Alpha", "Beta", "Charlie"],
#         "Zone": ["25AD", "30AD", "35AD"]
#     })
#     return df.to_dict(orient="records")

# Alternative

@app.get("/data")
def get_data(
    # Example URLs
    
    # https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv
    # https://jsonplaceholder.typicode.com/todos
    # https://jsonplaceholder.typicode.com/users/1
    url: str = Query("https://jsonplaceholder.typicode.com/users/1", description="Link to the dataset (CSV or JSON)")
):
    try:
        if url.endswith(".csv"):
            df = pd.read_csv(url)
        elif url.endswith(".xlsx"):
            df = pd.read_excel(url)
        else:
            resp = requests.get(url)
            resp.raise_for_status()

            try:
                data = resp.json()
                # if single object, then wrap list
                if isinstance(data, dict):
                    data = [data]
                df = pd.DataFrame(data)
            except ValueError:
                # If not JSON, fallback to CSV parser
                df = pd.read_csv(url)

        return df.to_dict(orient="records")

    except Exception as e:
        return {"error": str(e)}