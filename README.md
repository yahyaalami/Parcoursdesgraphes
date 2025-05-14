# Parcours DFS & BFS en Python

Ce projet implémente les algorithmes de parcours en profondeur (DFS) et en largeur (BFS) sur des graphes orientés, avec des options pour trier les parcours en ordre croissant ou décroissant. Il inclut également une visualisation graphique du graphe avec les résultats sous forme de tableau.


## Fonctionnalités

- ✅ Parcours DFS avec ordre croissant ou décroissant
- ✅ Parcours BFS avec ordre croissant ou décroissant
- ✅ Gestion automatique des composantes connexes
- ✅ Visualisation du graphe avec `networkx` et `matplotlib`
- ✅ Tableau récapitulatif des résultats des parcours

## Dépendances

Ce projet nécessite les bibliothèques suivantes :
bash
pip install matplotlib networkx
+```bash
+pip install matplotlib networkx
+```



## Utilisation
Exécutez le script Python et entrez le nœud de départ lorsque cela est demandé. Si vous entrez un nœud invalide, un nœud par défaut sera utilisé.

+```bash
+python dfs_bfs_graph.py
+```


## Exemple de graphe
graphe = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'C'],
    'C': ['E'],
    'D': ['F', 'C'],
    'E': ['A'],
    'F': ['C'],
    'G': ['D', 'F', 'H'],
    'H': ['C']
}


## Résultat Visuel

Une fenêtre matplotlib s'affiche montrant :

- Le graphe avec des flèches et des nœuds colorés (le nœud de départ en rouge)
- Un tableau présentant les résultats des parcours :

| Parcours                  | Résultats           |
|---------------------------|---------------------|
| DFS en ordre Croissant    | A → B → C → ...     |
| DFS en ordre Décroissant  | A → D → C → ...     |
| BFS en ordre Croissant    | A → B → C → ...     |
| BFS en ordre Décroissant  | A → D → C → ...     |



## Structure du projet
📁 dfs_bfs_project/
│

├── dfs_bfs_graph.py     # Script principal

├── README.md            # Documentation

└── Projet 1 Algo DFS & BFS.pdf   # Rapport du projet (optionnel)



## Remarques
Le code est conçu pour fonctionner avec des graphes orientés.
Il supporte automatiquement plusieurs composantes connexes.
Les résultats sont affichés graphiquement et dans le terminal (si les lignes correspondantes sont décommentées).

