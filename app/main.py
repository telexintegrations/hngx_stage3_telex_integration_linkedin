from fastapi import FastAPI, HTTPException 
from fastapi.responses import JSONResponse  
import requests   
import logging
from app.linkedin import fetch_linkedin_post_data  
from app.schemas import Settings, Output 
from app.config import LOAD_ENV  
import os
from dotenv import load_dotenv  
from fastapi.middleware.cors import CORSMiddleware  
from app.integration_info import integration_data  # Import the integration data  

app = FastAPI()  

logging.basicConfig(level=logging.INFO)

# Add CORS middleware  
origins = [  
    "https://telex.im",   
    "https://www.linkedin.com", 
    "https://staging.telex.im",
    "http://telextest.im",
    "http://staging.telextest.im",
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
        "message": "Post-stats-tracker for Linkedin is working!"
    }  

@app.get("/integration.json")  
async def get_integration_info():  
    return integration_data  # Return the integration data  

@app.post("/fetch-stats", response_model=Output)  
async def fetch_stats(settings: Settings):  
    if not settings.continue_monitoring:  
        raise HTTPException(status_code=400, detail="Monitoring is paused.")  

    try:  
        output = await fetch_linkedin_post_data(settings.post_url)  
        logging.info(f"Fetched stats: {output}")
        return output  
    except ValueError as e:  
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


# Function to send a notification to Telex webhook
def notification(post_stats: Output):
    """
    Send a notification to the Telex webhook with the provided metrics data.
    """
    url = "https://ping.telex.im/v1/webhooks/019537e2-5c8a-7fec-8994-7cf6ad7bb554"
    payload = {
        "event_name": "LinkedIn Post Monitoring",
        "message": f"Likes: {post_stats.likes}, Reposts: {post_stats.reposts}",
        "status": "success",
    }
    
    try:
        response = requests.post(url, json=payload, headers={"Accept": "application/json", "Content-Type": "application/json"})
        response.raise_for_status()  # This will throw an exception for 4xx or 5xx status codes
        logging.info(f"Notification sent successfully: {response.json()}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error sending notification: {e}")
        raise HTTPException(status_code=500, detail=f"Error sending notification: {e}")


@app.post("/tick")
async def tick(settings: Settings):
    try:
        # Fetch stats for the specified post URL
        output = await fetch_stats(settings)  # Get the stats data from fetch_stats
        # Send the notification with the metrics data (output is passed here)
        notification(output)  # Send the notification with the fetched data
        return output  # Return the fetched stats as the response
    except HTTPException as e:
        raise e  # Re-raise the HTTPException for proper status code and detail
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")