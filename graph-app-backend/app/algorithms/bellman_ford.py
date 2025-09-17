# bellman_ford.py
from typing import Dict, List, Tuple, Optional

def edgs_list(graphe: Dict[str, Dict[str, int]]) -> List[Tuple[str, str]]:
    """Renvoie la liste des arêtes sous forme de tuples (u,v)."""
    l = []
    for n in graphe:
        for nn in graphe[n]:
            l.append((n, nn))
    return l

def bellman_ford_opt_1(graphe: Dict[str, Dict[str, int]], edgs: List[Tuple[str,str]], origine: str
                       ) -> Tuple[bool, int, Dict[str,float], Dict[str,Optional[str]]]:
    """Retourne (valide, itérations, distances, prédécesseurs)."""
    dist = {n: float('inf') for n in graphe}
    pred = {n: None for n in graphe}
    dist[origine] = 0

    drop = True
    count = len(graphe) - 1
    it = 0

    while count > 0 and drop:
        drop = False
        it += 1
        for u, v in edgs:
            if dist[u] + graphe[u][v] < dist[v]:
                dist[v] = dist[u] + graphe[u][v]
                pred[v] = u
                drop = True
        count -= 1

    if drop:  # cycle négatif
        return False, it, dist, pred

    return True, it, dist, pred

def reconstruire_chemin(graphe: Dict[str, Dict[str,int]], edgs: List[Tuple[str,str]],
                        debut: str, fin: str) -> Tuple[List[str], float]:
    """Reconstruit le chemin le plus court et calcule le coût total."""
    l = []
    result = bellman_ford_opt_1(graphe, edgs, debut)
    valide, _, dist, pred = result

    if not valide:
        return [], float('inf')  # cycle négatif

    n = fin
    cout_total = 0
    while n != debut:
        if pred[n] is None:
            return [], float('inf')  # pas de chemin
        l.insert(0, n)
        cout_total += graphe[pred[n]][n]
        n = pred[n]
    l.insert(0, debut)
    return l, cout_total


def chemin_dist(graphe: Dict[str, Dict[str, int]], debut: str, fin: str) -> dict:
    edgs = edgs_list(graphe)
    chemin, cout_total = reconstruire_chemin(graphe, edgs, debut, fin)
    cycle_negatif = cout_total == float('inf')
    return {"chemin": chemin, "distance": cout_total, "cycle_negatif": cycle_negatif}