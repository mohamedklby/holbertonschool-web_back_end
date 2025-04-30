# NoSQL - MongoDB

This project includes MongoDB scripts and Python scripts that interact with MongoDB.

## MongoDB Scripts

- **0-list_databases**: Lists all databases
- **1-use_or_create_database**: Uses or creates a database
- **2-insert**: Inserts a document into a collection
- **3-all**: Lists all documents in a collection
- **4-match**: Finds documents with specific criteria
- **5-count**: Counts documents in a collection
- **6-update**: Updates documents in a collection
- **7-delete**: Deletes documents from a collection
- **8-update_many**: Updates multiple documents in a collection

## Python Scripts

- **12-log_stats.py**: Displays statistics about Nginx logs stored in MongoDB
- **restore_data.py**: Script to restore data from dump.zip

## Requirements

- MongoDB 4.4
- Python 3.7 or higher
- PyMongo

## Setup

1. Install MongoDB:
   ```
   sudo apt update
   sudo apt install -y mongodb
   ```

2. Start MongoDB:
   ```
   sudo service mongodb start
   ```

3. Import data:
   ```
   python3 restore_data.py
   ```

4. Run the log stats script:
   ```
   python3 12-log_stats.py
   ```

## Expected Output

When running `12-log_stats.py`, you should see output similar to:
```
94778 logs
Methods:
        method GET: 93842
        method POST: 229
        method PUT: 0
        method PATCH: 0
        method DELETE: 0
11614 status check
```

# MongoDB Scripts

Ce projet contient une collection de scripts MongoDB pour effectuer des opérations de base sur une base de données.

## Scripts MongoDB

### 0-list_databases
Liste toutes les bases de données disponibles sur le serveur MongoDB.
```bash
// List all databases
show dbs
```

### 1-use_or_create_database
Utilise ou crée une base de données nommée "my_db".
```bash
// Use or create a database
use my_db
```

### 2-insert
Insère un nouveau document dans la collection "school".
```bash
// Insert a document in the collection school
db.school.insertOne({ name: "Holberton school" })
```

### 3-find
Trouve tous les documents dans la collection "school".
```bash
// List all documents in the collection school
db.school.find()
```

### 4-update
Met à jour un document spécifique dans la collection "school".
```bash
// Update a document in the collection school
db.school.updateOne(
  { name: "Holberton school" },
  { $set: { address: "972 Mission street" } }
)
```

### 5-delete
Supprime un document spécifique de la collection "school".
```bash
// Delete a document from the collection school
db.school.deleteOne({ name: "Holberton school" })
```

### 6-count
Compte le nombre total de documents dans la collection "school".
```bash
// Count documents in the collection school
db.school.countDocuments()
```

### 7-list_collections
Liste toutes les collections dans la base de données actuelle.
```bash
// List all collections in the database
db.getCollectionNames()
```

### 8-update_many
Met à jour tous les documents qui ne correspondent pas aux critères spécifiés.
```bash
// Update all documents that don't match the criteria
db.users.updateMany(
  { likes: { $ne: "bananas" } },
  { $set: { likes: "bananas" } }
)
```

### 9-delete_many
Supprime tous les documents qui correspondent aux critères spécifiés.
```bash
// Delete all documents that match the criteria
db.users.deleteMany({ likes: "bananas" })
```

## Scripts Python

### 8-all.py
Liste tous les documents dans une collection MongoDB.
```python
#!/usr/bin/env python3
"""
Module to list all documents in a MongoDB collection.
"""
from typing import List, Dict


def list_all(mongo_collection) -> List[Dict]:
    """
    List all documents in a MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object

    Returns:
        A list of all documents in the collection
    """
    return list(mongo_collection.find())
```

### 9-insert_school.py
Insère un document dans une collection MongoDB.
```python
#!/usr/bin/env python3
"""
Module to insert a document into a MongoDB collection.
"""
from typing import Dict, Any


def insert_school(mongo_collection, **kwargs) -> str:
    """
    Insert a new document into a MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object
        **kwargs: The document fields to insert

    Returns:
        The _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
```

### 10-update_topics.py
Met à jour les sujets d'une école dans MongoDB.
```python
#!/usr/bin/env python3
"""
Module to update topics of a school document in MongoDB.
"""
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]) -> None:
    """
    Update the topics of a school document in MongoDB.

    Args:
        mongo_collection: The pymongo collection object
        name (str): The school name to update
        topics (list): The list of topics to set
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
```

### 11-schools_by_topic.py
Trouve les écoles par sujet dans MongoDB.
```python
#!/usr/bin/env python3
"""
Module to find schools by topic in MongoDB.
"""
from typing import List, Dict


def schools_by_topic(mongo_collection, topic: str) -> List[Dict]:
    """
    Find schools that have a specific topic.

    Args:
        mongo_collection: The pymongo collection object
        topic (str): The topic to search for

    Returns:
        A list of schools that have the specified topic
    """
    return list(mongo_collection.find({"topics": topic}))
```

### 12-log_stats.py
Fournit des statistiques sur les logs Nginx stockés dans MongoDB.
```python
#!/usr/bin/env python3
"""
Module to provide statistics about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


def log_stats():
    """
    Provide statistics about Nginx logs stored in MongoDB.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    # Count total logs
    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count logs by method
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    # Count logs with method=GET and path=/status
    status_count = logs_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_count} status check")


if __name__ == "__main__":
    log_stats()

## Utilisation

### Scripts MongoDB
Pour exécuter un script MongoDB, utilisez la commande suivante :
```bash
cat <nom_du_script> | mongo
```

Par exemple :
```bash
cat 0-list_databases | mongo
```

### Scripts Python
Pour exécuter un script Python, utilisez la commande suivante :
```bash
python3 <nom_du_script>.py
```

Par exemple :
```bash
python3 12-log_stats.py
```

## Notes

- Assurez-vous que MongoDB est installé et en cours d'exécution sur votre système
- Les scripts peuvent être modifiés selon vos besoins spécifiques
- Les commandes sont exécutées dans le shell MongoDB
- Tous les fichiers se terminent par une nouvelle ligne
- La première ligne de chaque fichier est un commentaire
- Les scripts Python utilisent PyMongo version 4.8.0 
