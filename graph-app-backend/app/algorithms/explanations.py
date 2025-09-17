explanations = {
    "dijkstra": """
Dijkstra est un algorithme de plus court chemin pour les graphes avec des poids positifs.
Il calcule la distance minimale de l'origine à tous les autres nœuds.
Le principe :
1. Initialiser toutes les distances à l'infini sauf l'origine (0).
2. Sélectionner le nœud avec la distance minimale non visitée.
3. Mettre à jour les distances des voisins si un chemin plus court est trouvé.
4. Répéter jusqu'à ce que tous les nœuds soient visités.
""",
    "bellman_ford": """
Bellman-Ford calcule les plus courts chemins même si certains poids sont négatifs.
Il peut détecter les cycles négatifs.
Le principe :
1. Initialiser les distances à l'infini sauf l'origine (0).
2. Relaxer toutes les arêtes V-1 fois (V = nombre de nœuds).
3. Vérifier si une relaxation supplémentaire est possible → cycle négatif.
""",
    "floyd_warshall": """
Floyd-Warshall calcule les plus courts chemins entre toutes les paires de nœuds.
Il utilise une approche matricielle et dynamique.
Le principe :
1. Créer une matrice des distances et des prédécesseurs.
2. Pour chaque nœud intermédiaire k, mettre à jour la distance i→j si i→k→j est plus court.
3. Répéter pour tous les nœuds intermédiaires.
4. Vérifier les cycles négatifs (dist[i][i] < 0).
"""
}

def get_explanation(algorithm_name: str) -> str:
    return explanations.get(algorithm_name.lower(), "Algorithme inconnu.")
