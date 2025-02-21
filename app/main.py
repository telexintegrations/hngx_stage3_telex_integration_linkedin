from fastapi import FastAPI, HTTPException  
from app.linkedin import fetch_linkedin_post_data  
from app.schemas import Settings, Output 
from app.config import LOAD_ENV  
import os
from dotenv import load_dotenv  
from fastapi.middleware.cors import CORSMiddleware  
from app.integration_info import integration_data  # Import the integration data  

app = FastAPI()  


# Add CORS middleware  
origins = [  
    "https://telex.im/",   
    "https://www.linkedin.com/", 
    "http://localhost:3000", 
    "https://ping.telex.im/v1/webhooks/0195058a-1518-764a-9db0-506a93c57aca",
     
]  

app.add_middleware(  
    CORSMiddleware,  
    allow_origins=origins,  # Allows the specified origins  
    allow_credentials=True,  
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)  
    allow_headers=["*"],  # Allows all headers  
) 

# Load environment variables from .env  
load_dotenv()  

# Access the API keys from environment variables  
LINKEDIN_API_KEY = os.getenv("LINKEDIN_API_KEY")  
LINKEDIN_API_SECRET = os.getenv("LINKEDIN_API_SECRET") 

@app.get("/")  
async def read_root():  
    return {
        "linkedin_api_key": LINKEDIN_API_KEY,  
        "linkedin_api_secret": LINKEDIN_API_SECRET  
        }  

@app.get("/integration-info")  
async def get_integration_info():  
    return integration_data  # Return the integration data  

@app.post("/fetch-stats", response_model=Output)  
async def fetch_stats(settings: Settings):  
    if not settings.continue_monitoring:  
        raise HTTPException(status_code=400, detail="Monitoring is paused.")  

    try:  
        output = await fetch_linkedin_post_data(settings.post_url)  
        return output  
    except ValueError as e:  
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/tick")  
async def tick():  
    return {"message": "Tick successful!"}