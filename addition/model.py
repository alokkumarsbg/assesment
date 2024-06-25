from pydantic import BaseModel
from typing import List
from datetime import datetime

class AdditionRequest(BaseModel):
    batchid: str
    lists: List[List[int]]

class AdditionResponse(BaseModel):
    batchid: str
    results: List[int]
    status: str
    started_at: datetime
    completed_at: datetime

