from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.route_planner_agent import plan_route

router = APIRouter(prefix="/route", tags=["Route Planner"])

# Added Pydantic model for validation
class RouteRequest(BaseModel):
    capability: dict
    opportunities: dict

@router.post("/")
def get_route(req: RouteRequest):
    return plan_route(req.capability, req.opportunities)