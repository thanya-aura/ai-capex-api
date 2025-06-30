from fastapi import FastAPI, UploadFile, File, Form, HTTPException
import pandas as pd
from io import BytesIO
from utils.analyzer import analyze_excel

app = FastAPI(title="CAPEX AI API", version="1.0")

@app.post("/analyze")
async def analyze(file: UploadFile = File(...), agent: str = Form(...)):
    if not file.filename.endswith((".xls", ".xlsx")):
        raise HTTPException(status_code=400, detail="Excel file only")

    contents = await file.read()
    df = pd.read_excel(BytesIO(contents))

    try:
        result = analyze_excel(df, agent_type=agent.lower())
        return {"agent": agent, "result": result if isinstance(result, dict) else result.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
