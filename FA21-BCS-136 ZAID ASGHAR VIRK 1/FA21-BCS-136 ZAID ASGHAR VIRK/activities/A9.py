import math

def calculate_perimeter(coordinates):
    if not isinstance(coordinates, list) or not all(isinstance(coord, tuple) and len(coord) == 2 for coord in coordinates):
        raise ValueError("Invalid input: coordinates must be a list of tuples (x, y).")

    perimeter = sum(
        math.sqrt((coordinates[i][0] - coordinates[i - 1][0])**2 + (coordinates[i][1] - coordinates[i - 1][1])**2)
        for i in range(1, len(coordinates))
    ) + math.sqrt((coordinates[0][0] - coordinates[-1][0])**2 + (coordinates[0][1] - coordinates[-1][1])**2)

    return perimeter

coordinates = [(1, 20), (35, 78), (2, 2), (0, 0)]
perimeter = calculate_perimeter(coordinates)
print(perimeter)