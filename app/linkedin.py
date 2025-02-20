import os  
import httpx  
from dotenv import load_dotenv  
from .schemas import Output  

load_dotenv()  

async def fetch_linkedin_post_data(post_url: str) -> Output:  
    linkedin_api_key = os.getenv("LINKEDIN_API_KEY")  
    headers = {  
        "Authorization": f"Bearer {linkedin_api_key}",  
        "Content-Type": "application/json"  
    }  
    
    # Extract post ID from URL  
    post_id = post_url.split('/')[-2]  
    
    # LinkedIn API call (modify based on the actual LinkedIn API)  
    response = await httpx.get(f"https://api.linkedin.com/v2/posts/{post_id}/likesAndShares", headers=headers)  

    if response.status_code == 200:  
        data = response.json()  
        likes = data.get('likes', 0)  
        reposts = data.get('shares', 0)  
        return Output(likes=likes, reposts=reposts)  
    else:  
        raise ValueError("Failed to fetch data from LinkedIn API.")