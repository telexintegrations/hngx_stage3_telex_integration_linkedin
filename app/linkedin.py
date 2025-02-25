import os  
import re
import httpx  
import logging
from dotenv import load_dotenv  
from app.schemas import Output  
from fastapi import HTTPException
from app.token_store import get_access_token 


load_dotenv()  

# Asynchronous function to fetch LinkedIn post data
logging.basicConfig(level=logging.INFO)

async def fetch_linkedin_post_data(post_url: str) -> dict:
    access_token = get_access_token()  # Retrieve the access token
    
    if not access_token:
        logging.error("Access token is missing or invalid.")
        raise HTTPException(status_code=401, detail="Access token is missing or invalid.")

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    # Extract the activity ID from the LinkedIn post URL
    match = re.search(r'activity:(\d+)', post_url)
    post_id = match.group(1) if match else None

    if not post_id:
        logging.error("Invalid LinkedIn post URL provided.")
        raise HTTPException(status_code=400, detail="Invalid LinkedIn post URL")

    try:
        # Correct API call to fetch post engagement data
        async with httpx.AsyncClient() as client:
            response = await client.get(f"https://api.linkedin.com/v2/socialActions/urn:li:activity:{post_id}", headers=headers)

        # Handle rate limiting
        if response.status_code == 429:
            logging.error(f"Rate limit exceeded for LinkedIn API. Status: {response.status_code}")
            raise HTTPException(status_code=429, detail="Rate limit exceeded by LinkedIn API")

        response.raise_for_status()  # Raise error for non-2xx responses
        data = response.json()

        # Extract engagement stats
        likes = data.get('likesSummary', {}).get('totalLikes', 0)
        reposts = data.get('sharesSummary', {}).get('totalShares', 0)

        logging.info(f"Post stats - Likes: {likes}, Reposts: {reposts}")
        return {"likes": likes, "reposts": reposts}

    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP Error: {e.response.status_code} - {e.response.text}")
        raise HTTPException(status_code=e.response.status_code, detail=f"HTTP error: {e.response.status_code} - {e.response.text}")

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")