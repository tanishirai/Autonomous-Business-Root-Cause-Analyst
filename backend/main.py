"""
FastAPI Backend for the Autonomous Analytics Investigator.
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.models import InvestigationRequest, InvestigationResponse
from agent.investigator import run_investigation

app = FastAPI(title="Autonomous Business Root-Cause Analyst API")

# Allow React frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "OK", "message": "Analytics Agent is running."}

@app.post("/investigate", response_model=InvestigationResponse)
def investigate(request: InvestigationRequest):
    """
    Main endpoint. Accepts a business question and returns a structured investigation.
    """
    try:
        # Run the AI agent
        result = run_investigation(request.question)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Investigation failed: {str(e)}")