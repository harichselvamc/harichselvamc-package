# harichselvamc

A simple Python package to generate Pascal's Triangle.

## Installation

You can install the package using pip:

```python 
pip install harichselvamc
```

## Usage
```python
from harichselvamc import generate_pascals_triangle
# Generate the first 5 rows of Pascal's Triangle
result = generate_pascals_triangle(5)
for row in result:
    print(row)
```