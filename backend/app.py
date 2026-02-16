"""
app.py — FastAPI backend for SCC Grader.
Run:
    cd backend
    uvicorn app:app --reload --port 8000
"""



from fastapi import FastAPI,File,UploadFile,Form,HTTPException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="SCC Grader API",
              description="Deep learning based grading squamous cell carcinoma",
              version="1.0.0"
              )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {"status": "ok","app":"Scc Grading"}

# prediction
