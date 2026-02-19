"""
A 3-Dimensional Valet Service
Demonstrates 2D and 3D lists (nested lists) in Python
"""

# -------------------------------------------------
# 2D List: index by row, then spot
# Structure: lot_2d[row][spot]
# -------------------------------------------------
lot_2d = [
    ['Toyota', 'Audi', 'BMW'],      # Row 0
    ['Lexus', 'Jeep'],              # Row 1
    ['Honda', 'Kia', 'Mazda']       # Row 2
]

# -------------------------------------------------
# 3D List: index by floor, then row, then spot
# Structure: lot_3d[floor][row][spot]
# -------------------------------------------------
lot_3d = [
    [   # Floor 0
        ['Tesla', 'Fiat', 'BMW'],
        ['Honda', 'Jeep'],
        ['Saab', 'Kia', 'Ford']
    ],
    [   # Floor 1
        ['Subaru', 'Nissan'],
        ['Volvo']
    ],
    [   # Floor 2
        ['Mazda', 'Chevy'],
        [],                     # Empty row (no cars parked)
        ['Volkswagen']
    ]
]

# -------------------------------------------------
# Demo
# -------------------------------------------------
if __name__ == '__main__':

    # -----------------------------
    # Indexing 2D List
    # -----------------------------
    print("Full 2D lot:")
    print(lot_2d)

    print("\nRow 2:")
    print(lot_2d[2])  # Entire row

    print("\nCar at row 2, spot 1:")
    print(lot_2d[2][1])  # Specific car

    # -----------------------------
    # Indexing 3D List
    # -----------------------------
    print("\nFull 3D lot:")
    print(lot_3d)

    print("\nFloor 0:")
    print(lot_3d[0])  # Entire floor

    print("\nFloor 0, Row 2:")
    print(lot_3d[0][2])  # Entire row on a floor

    print("\nFloor 0, Row 2, Spot 1:")
    print(lot_3d[0][2][1])  # Specific car

    # -----------------------------
    # Iterating through all cars
    # -----------------------------
    print("\nAll cars in the garage:")
    for floor in lot_3d:
        for row in floor:
            for car in row:
                print(car)