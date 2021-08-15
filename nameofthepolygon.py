num_sides = int(input())
if num_sides < 3:
    print("Not Polygon")
elif num_sides == 3:
    print("Triangle")
elif num_sides == 4:
    print("Quadrilateral")
elif num_sides == 5:
    print("Pentagon")
else:
    print("Big Polygon")