from pydantic import BaseModel  
from typing import List, Optional 

class Output(BaseModel):  
    likes: int  
    reposts: int   
    
    @root_validator(pre=True)
    def cast_values(cls, values):
        # Ensure likes and reposts are integers
        if 'likes' in values:
            values['likes'] = int(values.get('likes', 0))  # Cast likes to integer
        if 'reposts' in values:
            values['reposts'] = int(values.get('reposts', 0))  # Cast reposts to integer
        return values

class Settings(BaseModel):  
    post_url: str  
    interval: str  
    #alert_admin: List[str]  
    sensitivity_level: str  
    provide_speed: Optional[int] = 1  
    continue_monitoring: bool  