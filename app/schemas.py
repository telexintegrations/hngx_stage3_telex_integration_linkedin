from pydantic import BaseModel  
from typing import List, Optional 

class Output(BaseModel):  
    likes: int  
    reposts: int   

class Settings(BaseModel):  
    post_url: str  
    interval: str  
    #alert_admin: List[str]  
    sensitivity_level: str  
    provide_speed: Optional[int] = None  
    continue_monitoring: bool  