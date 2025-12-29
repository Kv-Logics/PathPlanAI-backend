from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.opportunity_agent import match_opportunities

router = APIRouter(prefix="/opportunities", tags=["Opportunities"])

class SkillInput(BaseModel):
    skills: list[str]

@router.post("/")
def get_opportunities(data: SkillInput):
    return match_opportunities(data.skills)
