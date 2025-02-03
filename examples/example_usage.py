from harichselvamc import generate_pascals_triangle, get_wifi_password

# Generate Pascal's Triangle for 7 rows
rows = 7
triangle = generate_pascals_triangle(rows)

# Print each row of the triangle
print("Pascal's Triangle:")
for row in triangle:
    print(row)

# Get Wi-Fi password for a given network
network_name = "YourNetworkName"
wifi_password = get_wifi_password(network_name)

# Print the Wi-Fi password
print(f"\nWi-Fi password for '{network_name}': {wifi_password}")
