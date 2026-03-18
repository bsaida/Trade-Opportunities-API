from fastapi import FastAPI, Depends, HTTPException, Request
from auth import verify_token, create_token
from rate_limiter import limiter
from slowapi.middleware import SlowAPIMiddleware
from services.data_collector import fetch_market_data
from services.ai_analyzer import analyze_data
from utils.session_manager import track_session

app = FastAPI(title="Trade Opportunities API")

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.get("/")
def home():
    return {"message": "Trade Opportunities API running"}

@app.get("/token")
def get_token(username: str):
    return {"token": create_token(username)}

@app.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze_sector(request: Request, sector: str, user=Depends(verify_token)):
    
    if not sector.isalpha():
        raise HTTPException(status_code=400, detail="Invalid sector")

    session = track_session(user)

    try:
        data = await fetch_market_data(sector)
        report = await analyze_data(sector, data)

        return {
            "user": user,
            "requests_made": session["requests"],
            "sector": sector,
            "report": report
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))