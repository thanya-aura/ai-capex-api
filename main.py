from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import HTMLResponse
import pandas as pd
from io import BytesIO
from utils.analyzer import analyze_excel

app = FastAPI(title="CAPEX AI API", version="1.0")

# ✅ Health check route for Render
@app.get("/", response_class=HTMLResponse)
async def root():
    return "<h3>✅ CAPEX AI API is running! Visit /docs for usage.</h3>"

# ✅ Analysis endpoint
@app.post("/analyze")
async def analyze(file: UploadFile = File(...), agent: str = Form(...)):
    if not file.filename.endswith((".xls", ".xlsx")):
        raise HTTPException(status_code=400, detail="❌ Excel file only (.xls or .xlsx)")

    try:
        contents = await file.read()
        df = pd.read_excel(BytesIO(contents))

        result = analyze_excel(df, agent_type=agent.lower())
        return {
            "agent": agent,
            "result": result if isinstance(result, dict) else result.to_dict()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ Error analyzing file: {str(e)}")
