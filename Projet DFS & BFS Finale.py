import matplotlib.pyplot as plt
import networkx as nx 

from collections import deque

# Fonction pour gérer toutes les composantes connexes avec un nœud de départ
def dfs_global(graph, start_node=None, order='ascending'):
    visited = set()
    result = []
    all_nodes = sorted(graph.keys(), reverse=(order == 'descending'))  # Trier les nœuds tout en respectant l'ordre demandé
    sort_function = sorted if order == 'ascending' else lambda x: sorted(x, reverse=True)  # Choisir l'ordre de tri pour les voisins
    current_node = start_node if start_node is not None else all_nodes[0]  # Si un nœud de départ est spécifié, commencer par celui-ci
    while len(visited) < len(graph):  # Répéter jusqu'à ce que tous les nœuds soient visités
        if current_node not in visited:
            dfs_component(graph, current_node, visited, result, sort_function)
        # Trouver le prochain nœud non visité
        for node in all_nodes:
            if node not in visited:
                current_node = node
                break
    return result

# Fonction DFS pour une composante donnée
def dfs_component(graph, node, visited, result, sort_function):
    if node not in visited:
        visited.add(node)
        for neighbor in sort_function(graph[node]):
            if neighbor not in visited:
                dfs_component(graph, neighbor, visited, result, sort_function)
        result.append(node)

def bfs_global(graph, start_node=None, order="asc"):
    visited = set()
    result = []
    all_nodes = sorted(graph.keys(), reverse=(order == "desc"))  # Trier les nœuds tout en respectant l'ordre demandé
    queue = deque([start_node] if start_node else [all_nodes[0]])  # Démarrer par le nœud donné ou le premier nœud déclaré
    while len(visited) < len(graph):  # Répéter jusqu'à ce que tous les nœuds soient visités
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                # Ajouter les voisins triés dans la file d'attente
                neighbors = sorted(graph.get(node, []), reverse=(order == "desc"))
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
        # Trouver le prochain nœud non visité et le rajouter dans la file
        for node in all_nodes:
            if node not in visited:
                queue.append(node)
                break
    return result


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

# Fonction pour valider et convertir le nœud de départ
def get_start_node(graph, input_node):
    try:
        # Essayer de convertir en entier si possible
        input_node = int(input_node) if input_node.isdigit() else input_node
        if input_node in graph:
            return input_node
    except ValueError:
        pass
    print("Le nœud entré n'est pas valide. Un nœud par défaut sera utilisé.")
    return list(graph.keys())[0]  # Utiliser le premier nœud par défaut

# Demander à l'utilisateur de choisir un nœud de départ
user_input = input("Entrez le nœud de départ: ").strip()
start_node = get_start_node(graphe, user_input)

# Parcours DFS et BFS
result_ascending = dfs_global(graphe, start_node=start_node, order='ascending')
result_descending = dfs_global(graphe, start_node=start_node, order='descending')
result_croissant = bfs_global(graphe, start_node=start_node, order="asc")
result_decroissant = bfs_global(graphe, start_node=start_node, order="desc")

# Résultats
#print("Parcours en profondeur DFS en ordre croissant   : ", " - ".join(map(str, result_ascending)))
#print("Parcours en profondeur DFS en ordre décroissant : ", " - ".join(map(str, result_descending)))
#print("Parcours en largeur    BFS en ordre croissant   : ", " - ".join(map(str, result_croissant)))
#print("Parcours en largeur    BFS en ordre décroissant : ", " - ".join(map(str, result_decroissant)))


# Code pour afficher le graphe avec un agencement en cercle
G = nx.DiGraph()  # Utilisation d'un graphe dirigé pour les flèches
for node, neighbors in graphe.items():   # Ajouter les noeuds et les arêtes au graphe
    for neighbor in neighbors:
        G.add_edge(node, neighbor)
pos = nx.circular_layout(G) # Choisir un layout circulaire pour arranger les nœuds en cercle
node_colors = ['red' if node == start_node else 'skyblue' for node in G.nodes()] # Définir la couleur des nœuds
# Créer une figure à la fois le graphe et le tableau
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))  # Taille du graphe et du tableau
# Dessiner le graphe dans le premier axe (ax1)
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=2000, font_size=16, font_weight='bold', edge_color='gray', arrows=True, ax=ax1)
#--------------------ax1.set_title("Présentation du Graphe")
# Affichage du tableau dans le deuxième axe (ax2)
table_data = [
    ["DFS en ordre Croissant", result_ascending],
    ["DFS en ordre Décroissant", result_descending],
    ["BFS en ordre Croissant", result_croissant],
    ["BFS en ordre Décroissant", result_decroissant]
]
ax2.axis('off') # Désactiver les axes pour le tableau
# Afficher le tableau dans ax2
table = ax2.table(cellText=table_data, colLabels=["Parcours", "Résultats"], cellLoc='center', loc='center', colColours=["lightblue", "lightgreen"])
# Modifier la hauteur des lignes (données)
for key, cell in table.get_celld().items():
    if key[0] != 0:  # Eviter la ligne d'entête
        cell.set_height(0.1)  # Ajuster la hauteur des lignes
        cell.set_fontsize(25)  # Modifier la taille de la police pour les cellules de données
        cell.set_text_props(fontweight='bold')  # Rendre la police de l'en-tête en gras
# Modifier la hauteur et le style des cellules d'entête (colLabels)
for cell in table.get_celld().values():
    if cell.get_text() is not None:  # S'assurer que la cellule contient du texte
        cell.set_height(0.08)  # Ajuster la hauteur de l'en-tête
        cell.set_fontsize(25)  # Modifier la taille de la police pour les cellules d'en-tête
        cell.set_text_props(fontweight='bold')  # Rendre la police de l'en-tête en gras

# Fixer la taille de la fenêtre d'affichage (en pouces)
fig.set_size_inches(16, 7)  # (Largeur,Hauteur)
# Afficher l'ensemble
plt.tight_layout()  # Ajuster pour un meilleur espacement
plt.show()
