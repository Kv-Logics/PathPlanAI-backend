def plan_route(capability, opportunities):
    readiness = capability["readiness_score"]

    if readiness < 40:
        return {
            "route": "Skill First",
            "reason": "Low readiness score. Focus on learning and projects before applying.",
            "next_actions": [
                "Complete 2 backend projects",
                "Learn FastAPI + SQL",
                "Build GitHub portfolio"
            ]
        }

    if readiness < 70:
        return {
            "route": "Balanced",
            "reason": "Moderate readiness. Apply selectively while improving skills.",
            "next_actions": [
                "Apply to safe opportunities",
                "Participate in one hackathon",
                "Improve resume"
            ]
        }

    return {
        "route": "Apply First",
        "reason": "High readiness. Focus on applications and interviews.",
        "next_actions": [
            "Apply to stretch roles",
            "Prepare for interviews",
            "Mock interviews"
        ]
    }
