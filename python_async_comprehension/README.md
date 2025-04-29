
n Async Comprehension

This project demonstrates the use of async generators and comprehensions in Python.
It includes three main components:

1. `0-async_generator.py`: An async generator that yields random numbers
2. `1-async_comprehension.py`: Uses async comprehension to collect random numbers
3. `2-measure_runtime.py`: Measures the runtime of parallel async comprehensions

## Requirements

- Python 3.9
- Ubuntu 20.04 LTS
- pycodestyle 2.5.x

## Usage

Each file can be run independently:

```bash
python3 0-main.py  # Run the async generator
python3 1-main.py  # Run the async comprehension
python3 2-main.py  # Measure runtime of parallel comprehensions
```

## Features

- Async generators with random number generation
- Async comprehensions for collecting values
- Parallel execution with asyncio.gather
- Runtime measurement for performance analysis
