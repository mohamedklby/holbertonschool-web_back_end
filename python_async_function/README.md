# Python Async Function

Ce projet contient des exemples d'utilisation de fonctions asynchrones en Python avec le module `asyncio`.

## Structure du projet

- `0-basic_async_syntax.py` : Implémente une fonction asynchrone de base qui attend un délai aléatoire
- `1-concurrent_coroutines.py` : Exécute plusieurs coroutines en parallèle et retourne les résultats triés
- `2-measure_runtime.py` : Mesure le temps d'exécution des coroutines
- `3-tasks.py` : Crée des tâches asyncio à partir de coroutines
- `4-tasks.py` : Exécute plusieurs tâches en parallèle et retourne les résultats triés

## Fonctionnalités

### 0-basic_async_syntax.py
- `wait_random(max_delay: int = 10) -> float` : Attend un délai aléatoire entre 0 et max_delay secondes

### 1-concurrent_coroutines.py
- `wait_n(n: int, max_delay: int) -> List[float]` : Exécute wait_random n fois en parallèle et retourne les délais triés

### 2-measure_runtime.py
- `measure_time(n: int, max_delay: int) -> float` : Mesure le temps moyen d'exécution de wait_n

### 3-tasks.py
- `task_wait_random(max_delay: int) -> asyncio.Task` : Crée une tâche asyncio qui attend un délai aléatoire

### 4-tasks.py
- `task_wait_n(n: int, max_delay: int) -> List[float]` : Exécute task_wait_random n fois en parallèle et retourne les délais triés

## Exemples d'utilisation

```python
# Exemple d'utilisation de wait_random
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
print(asyncio.run(wait_random()))  # Délai aléatoire entre 0 et 10 secondes
print(asyncio.run(wait_random(5)))  # Délai aléatoire entre 0 et 5 secondes

# Exemple d'utilisation de wait_n
wait_n = __import__('1-concurrent_coroutines').wait_n
print(asyncio.run(wait_n(5, 5)))  # 5 délais aléatoires entre 0 et 5 secondes, triés

# Exemple d'utilisation de measure_time
measure_time = __import__('2-measure_runtime').measure_time
print(measure_time(5, 9))  # Temps moyen d'exécution de 5 tâches avec max_delay=9

# Exemple d'utilisation de task_wait_random
task_wait_random = __import__('3-tasks').task_wait_random
task = task_wait_random(5)
print(asyncio.run(task))  # Délai aléatoire entre 0 et 5 secondes

# Exemple d'utilisation de task_wait_n
task_wait_n = __import__('4-tasks').task_wait_n
print(asyncio.run(task_wait_n(5, 6)))  # 5 délais aléatoires entre 0 et 6 secondes, triés
```

## Notes

- Les résultats sont triés sans utiliser la méthode `sort()` pour respecter la concurrence
- Le temps d'exécution est mesuré avec le module `time`
- Les tâches asyncio sont créées avec `asyncio.create_task()`
- Les coroutines sont exécutées en parallèle avec `asyncio.gather()` 
