from harichselvamc import generate_triangle

# Generate Pascal's Triangle for 7 rows
rows = 7
triangle = generate_triangle(rows)

# Print each row of the triangle
for row in triangle:
    print(row)