import os  
import httpx  
from dotenv import load_dotenv  
from .schemas import Output  
from fastapi import HTTPException

load_dotenv()  

# Asynchronous function to fetch LinkedIn post data
async def fetch_linkedin_post_data(post_url: str) -> Output:
    linkedin_api_key = os.getenv("LINKEDIN_API_KEY")
    
    if not linkedin_api_key or not linkedin_api_secret:
        raise HTTPException(status_code=500, detail="LinkedIn API credentials not found in environment variables.")

    headers = {
        "Authorization": f"Bearer {linkedin_api_key}",
        "Content-Type": "application/json"
    }

    # Extract post ID from the URL (assuming it's in the standard format)
    post_id = post_url.split('/')[-2]  

    try:
        # Make an asynchronous HTTP request
        async with httpx.AsyncClient() as client:
            response = await client.get(f"https://api.linkedin.com/v2/posts/{post_id}/likesAndShares", headers=headers)
        # Raise an exception for 4xx or 5xx status codes
        if response.status_code == 429:
            raise HTTPException(status_code=429, detail="Rate limit exceeded by LinkedIn API")
        response.raise_for_status()
        data = await response.json()
        likes = int(data.get('likes', 0)) # extract likes from the data
        reposts = int(data.get('shares', 0)) #extract post from the data
        return Output(likes=likes, reposts=reposts) # return output 

    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP Error: {e.response.status_code} - {e.response.text}")
        raise HTTPException(status_code=e.response.status_code, detail=f"HTTP error: {e.response.status_code} - {e.response.text}")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
