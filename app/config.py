import os  
from dotenv import load_dotenv  

def LOAD_ENV():  
    load_dotenv()  

# Access variables  
LINKEDIN_API_KEY = os.getenv('LINKEDIN_API_KEY')  
LINKEDIN_API_SECRET = os.getenv('LINKEDIN_API_SECRET')  