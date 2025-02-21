from fastapi import FastAPI, HTTPException  
from app.linkedin import fetch_linkedin_post_data  
from app.schemas import Settings, Output 
from app.config import LOAD_ENV  
from app.integration_info import integration_data  # Import the integration data  

app = FastAPI()  


# Add CORS middleware  
origins = [  
    "https://telex.im/",  # Add your frontend URL here  
    "https://www.linkedin.com/", 
    "http://localhost:3000", 
    # Include any other allowed origins as needed  
]  

app.add_middleware(  
    CORSMiddleware,  
    allow_origins=origins,  # Allows the specified origins  
    allow_credentials=True,  
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)  
    allow_headers=["*"],  # Allows all headers  
) 

@app.on_event("startup")  
async def startup_event():  
    LOAD_ENV()  # Load environment variables if needed  

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