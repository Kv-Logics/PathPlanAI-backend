from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.capability_agent import build_capability_map

router = APIRouter(prefix="/capability", tags=["Capability"])


class ResumeInput(BaseModel):
    resume_text: str


@router.post("/")
def analyze_capability(data: ResumeInput):
    result = build_capability_map(data.resume_text)
    return result
