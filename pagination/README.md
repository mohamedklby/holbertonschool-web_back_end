# Pagination

Ce projet implémente différentes stratégies de pagination pour une API de données sur les noms de bébés populaires.

## Structure du projet

Le projet est composé de quatre fichiers principaux :

1. `0-simple_helper_function.py` : Fonction utilitaire pour calculer les indices de pagination
2. `1-simple_pagination.py` : Implémentation basique de la pagination
3. `2-hypermedia_pagination.py` : Pagination avec métadonnées hypermédia
4. `3-hypermedia_del_pagination.py` : Pagination résistante aux suppressions

## Fonctionnalités

### 0-simple_helper_function.py
- `index_range(page, page_size)` : Calcule les indices de début et de fin pour une page donnée
- Les pages sont indexées à partir de 1 (1-indexed)

### 1-simple_pagination.py
- Classe `Server` pour gérer un jeu de données CSV
- Méthode `get_page(page, page_size)` pour récupérer une page de données
- Vérification des arguments avec `assert`

### 2-hypermedia_pagination.py
- Étend la pagination simple avec des métadonnées hypermédia
- Méthode `get_hyper(page, page_size)` qui retourne :
  - `page_size` : taille de la page
  - `page` : numéro de page actuel
  - `data` : données de la page
  - `next_page` : numéro de la page suivante
  - `prev_page` : numéro de la page précédente
  - `total_pages` : nombre total de pages

### 3-hypermedia_del_pagination.py
- Implémente une pagination résistante aux suppressions
- Utilise un dictionnaire indexé pour stocker les données
- Méthode `get_hyper_index(index, page_size)` qui retourne :
  - `index` : index de début actuel
  - `data` : données de la page
  - `page_size` : taille de la page
  - `next_index` : prochain index à utiliser

## Utilisation

```python
# Exemple d'utilisation de la pagination simple
from pagination.1-simple_pagination import Server

server = Server()
page_data = server.get_page(page=1, page_size=10)
print(page_data)

# Exemple d'utilisation de la pagination hypermédia
from pagination.2-hypermedia_pagination import Server

server = Server()
hyper_data = server.get_hyper(page=1, page_size=10)
print(hyper_data)

# Exemple d'utilisation de la pagination résistante aux suppressions
from pagination.3-hypermedia_del_pagination import Server

server = Server()
index_data = server.get_hyper_index(index=0, page_size=10)
print(index_data)
```

## Fichier de données

Le projet utilise le fichier `Popular_Baby_Names.csv` qui contient des données sur les noms de bébés populaires avec les colonnes suivantes :
- Year of Birth
- Gender
- Ethnicity
- Child's First Name
- Count
- Rank
