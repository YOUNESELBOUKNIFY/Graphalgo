# dijkstra.py
from typing import Dict, Tuple, List

def min_distance(Q: List[str], dist: Dict[str, float]) -> str:
    min_noeud = None
    min_dist = float('inf')
    for noeud in Q:
        if dist[noeud] < min_dist:
            min_dist = dist[noeud]
            min_noeud = noeud
    return min_noeud

def dijkstra(graphe: Dict[str, Dict[str, int]], origine: str) -> Tuple[Dict[str, float], Dict[str, str]]:
    dist = {n: float('inf') for n in graphe}
    pred = {n: None for n in graphe}
    dist[origine] = 0
    Q = list(graphe.keys())

    while Q:
        n_min_d = min_distance(Q, dist)
        Q.remove(n_min_d)

        for voisin, poids in graphe[n_min_d].items():
            tmp = dist[n_min_d] + poids
            if dist[voisin] > tmp:
                dist[voisin] = tmp
                pred[voisin] = n_min_d

    return dist, pred

def reconstruire_chemin(graphe: Dict[str, Dict[str, int]], pred: Dict[str, str], debut: str, fin: str) -> Tuple[List[str], float]:
    chemin = []
    cout_total = 0
    n = fin
    while n != debut:
        if pred[n] is None:
            return [], float('inf')
        chemin.insert(0, n)
        cout_total += graphe[pred[n]][n]
        n = pred[n]
    chemin.insert(0, debut)
    return chemin, cout_total


def chemin_dist(graphe: Dict[str, Dict[str, int]], debut: str, fin: str) -> dict:
    dist, pred = dijkstra(graphe, debut)
    chemin, cout_total = reconstruire_chemin(graphe, pred, debut, fin)
    return {"chemin": chemin, "distance": cout_total}
