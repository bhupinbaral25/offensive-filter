from typing import Optional
from pydantic import BaseModel

class ChatQuery(BaseModel):
    chat: str
    
class OutputResponse(BaseModel):
    offensive: bool
    confidence_score: Optional[float]
