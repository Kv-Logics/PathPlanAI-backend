from fastapi import FastAPI

from app.routes.capability import router as capability_router
from app.routes.opportunity import router as opportunity_router
from app.routes.route_planner import router as route_router

app = FastAPI(
    title="PathPlanAI Backend",
    version="0.1.0"
)

# Register routers
app.include_router(capability_router)
app.include_router(opportunity_router)
app.include_router(route_router)

# Health check
@app.get("/")
def health_check():
    return {"status": "ok"}
