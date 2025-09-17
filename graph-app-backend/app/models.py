from pydantic import BaseModel
from typing import Dict

class GraphRequest(BaseModel):
    graphe: Dict[str, Dict[str,int]]
    debut: str
    fin: str
