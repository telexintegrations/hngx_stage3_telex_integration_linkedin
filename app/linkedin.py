import os  
import httpx  
import logging
from dotenv import load_dotenv  
from app.schemas import Output  
from fastapi import HTTPException
from app.token_store import access_token_store
from app.token_store import get_access_token

load_dotenv()  

# Asynchronous function to fetch LinkedIn post data
logging.basicConfig(level=logging.INFO)

async def fetch_linkedin_post_data(post_url: str) -> Output:
    
    access_token = get_access_token()
    
    if not access_token_store:
        logging.error("Access token is missing or invalid.")
        raise HTTPException(status_code=401, detail="Access token is missing or invalid.")
    headers = {
        "Authorization": f"Bearer {access_token_store}",
        "Content-Type": "application/json"
    }

    # Extract post ID from the URL
    post_id = post_url.split('/')[-2]
    logging.info(f"Fetching data for post ID: {post_id}")

    try:
        # Make an asynchronous HTTP request
        async with httpx.AsyncClient() as client:
            response = await client.get(f"https://api.linkedin.com/v2/posts/{post_id}/likesAndShares", headers=headers)   
        if response.status_code == 429:
            logging.error(f"Rate limit exceeded for LinkedIn API. Status: {response.status_code}")
            raise HTTPException(status_code=429, detail="Rate limit exceeded by LinkedIn API")
        response.raise_for_status()  # Raise for any other errors
        data = response.json()
        # Log the fetched data for debugging (be cautious of sensitive data)
        logging.info(f"Fetched data for post: {data}")
        likes = int(data.get('likes', 0))
        reposts = int(data.get('shares', 0))        
        logging.info(f"Post stats - Likes: {likes}, Reposts: {reposts}")
        return Output(likes=likes, reposts=reposts)
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP Error: {e.response.status_code} - {e.response.text}")
        raise HTTPException(status_code=e.response.status_code, detail=f"HTTP error: {e.response.status_code} - {e.response.text}")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")