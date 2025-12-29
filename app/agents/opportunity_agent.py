import json
from pathlib import Path
from typing import List, Dict

DATA_PATH = Path("data/opportunities.json")

def load_opportunities() -> List[Dict]:
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def match_opportunities(user_skills: List[str]) -> Dict:
    opportunities = load_opportunities()

    result = {
        "safe": [],
        "stretch": [],
        "aspirational": []
    }

    for opp in opportunities:
        required = set(opp["required_skills"])
        matched = required.intersection(set(user_skills))

        if len(matched) > 0:
            result[opp["difficulty"]].append({
                "title": opp["title"],
                "type": opp["type"],
                "matched_skills": list(matched)
            })

    return result
