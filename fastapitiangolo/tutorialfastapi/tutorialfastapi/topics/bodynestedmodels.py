from fastapi import APIRouter
from pydantic import BaseModel,Field
from typing import Optional,List

class Piaic(BaseModel):
    name: str 
    description: Optional[str] = None
    courses: List[str]=Field(min_items=1, max_items=4)
    fees:int 
    teachers:set[str]
    
    

router = APIRouter()

@router.post("/bodynestedmodels",response_model=Piaic)
async def read_root(Piaic: Piaic):
    return Piaic