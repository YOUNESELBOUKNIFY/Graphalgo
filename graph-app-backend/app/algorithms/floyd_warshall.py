# floyd_warshall.py
import numpy as np
from typing import Dict, List, Tuple

def mapping_graphe(graphe: Dict[str, Dict[str,int]]) -> Dict[str,int]:
    return {k: i for i, k in enumerate(graphe.keys())}

def create_edgs(graphe: Dict[str, Dict[str,int]]) -> List[Tuple[str,str,int]]:
    return [(u, v, w) for u in graphe for v, w in graphe[u].items()]

def ini_matrice(graphe: Dict[str, Dict[str,int]], mapping: Dict[str,int], edgs: List[Tuple[str,str,int]]):
    n = len(graphe)
    dist = np.full((n, n), float('inf'))
    pred = np.full((n, n), None, dtype=object)
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edgs:
        dist[mapping[u]][mapping[v]] = w
        pred[mapping[u]][mapping[v]] = u
    return dist, pred

def algorithm_floyd_warshall(graphe: Dict[str, Dict[str,int]]):
    edgs = create_edgs(graphe)
    mapping = mapping_graphe(graphe)
    dist, pred = ini_matrice(graphe, mapping, edgs)
    n = len(graphe)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    # Vérification des cycles négatifs
    for i in range(n):
        if dist[i][i] < 0:
            return False, dist, pred

    return True, dist, pred, mapping

def reconstruire_chemin(pred, mapping: Dict[str,int], debut: str, fin: str) -> List[str]:
    chemin = []
    i, j = mapping[debut], mapping[fin]
    while debut != fin:
        chemin.append(fin)
        fin = pred[i][j]
        i, j = mapping[debut], mapping[fin]
    chemin.append(debut)
    chemin.reverse()
    return chemin

# Fonction standard pour l'API FastAPI
def chemin_dist(graphe: Dict[str, Dict[str,int]], debut: str, fin: str) -> dict:
    valide, dist, pred, mapping = algorithm_floyd_warshall(graphe)
    if not valide:
        return {"chemin": [], "distance": float('inf'), "cycle_negatif": True}
    chemin = reconstruire_chemin(pred, mapping, debut, fin)
    distance = dist[mapping[debut]][mapping[fin]]
    return {"chemin": chemin, "distance": distance, "cycle_negatif": False}
