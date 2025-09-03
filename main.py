from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
from pydantic import BaseModel
from typing import List
import pandas as pd
import joblib
import io


app = FastAPI(title="Exoplanet Detection API")

model = joblib.load("rf_pipeline.pkl")


class PredictionResponse(BaseModel):
    predictions: List[str]

async def read_csv_file(file: UploadFile):
    if not file.filename.endswith(".csv"):
        raise ValueError("Invalid file format. Please upload a .csv file")

    contents = await file.read()
    try:
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))
    except Exception as e:
        raise ValueError(f"Error reading CSV: {str(e)}")
    return df


@app.post("/predict_csv/")
async def predict_csv(file: UploadFile = File(...)):
    try:
        df = await read_csv_file(file)
        predictions = model.predict(df)
        df["prediction"] = predictions

        output = io.StringIO()
        df.to_csv(output, index=False)
        output.seek(0)

        return StreamingResponse(
            iter([output.getvalue()]),
            media_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=predictions.csv"}
        )
    except ValueError as e:
        return JSONResponse(status_code=400, content={"error": str(e)})


@app.post("/predict_json/", response_model=PredictionResponse)
async def predict_json(file: UploadFile = File(...)):
    try:
        df = await read_csv_file(file)
        predictions = model.predict(df)
        readable = ["Exoplanet" if p == 1 else "Not Exoplanet" for p in predictions]
        return {"predictions": readable}
    except ValueError as e:
        return JSONResponse(status_code=400, content={"error": str(e)})


@app.get("/")
def home():
    return {"message": "✅ Exoplanet Detection API is running!"}
