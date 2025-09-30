from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os

app = FastAPI()

# Allow frontend to connect (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://campaign-analytics-frontend.vercel.app"], # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# PostgreSQL connection using Render's DATABASE_URL
DATABASE_URL = os.environ.get("DATABASE_URL")  # Render provides this
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# API endpoint to get campaigns
@app.get("/campaigns")
def get_campaigns(status: str = None):
    try:
        with SessionLocal() as db:
            query = "SELECT id, name, status, clicks, cost, impressions FROM campaigns"
            params = {}

            if status:
                query += " WHERE LOWER(status) = LOWER(:status)"
                params["status"] = status

            result = db.execute(text(query), params)

            campaigns = [
                {
                    "id": row[0],
                    "name": row[1],
                    "status": row[2],
                    "clicks": row[3],
                    "cost": row[4],
                    "impressions": row[5]
                }
                for row in result
            ]
            return campaigns
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")