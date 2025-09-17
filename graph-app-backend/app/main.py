from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import GraphRequest
from app.algorithms import dijikstra, bellman_ford, floyd_warshall
from app.algorithms.explanations import get_explanation
app = FastAPI(title="API Graphes")

# CORS pour React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def racine():
    return {"message": "Backend Graphes OK 🚀"}

@app.post("/dijkstra")
def chemin_dijkstra(data: GraphRequest):
    return dijikstra.chemin_dist(data.graphe, data.debut, data.fin)

@app.post("/bellman-ford")
def chemin_bellman_ford(data: GraphRequest):
    return bellman_ford.chemin_dist(data.graphe, data.debut, data.fin)

@app.post("/floyd-warshall")
def chemin_floyd_warshall(data: GraphRequest):
    return floyd_warshall.chemin_dist(data.graphe, data.debut, data.fin)

# A* à compléter si besoin


@app.get("/explain/{algorithm_name}")
def explain_algorithm(algorithm_name: str):
    texte = get_explanation(algorithm_name)
    return {"algorithme": algorithm_name, "explication": texte}
