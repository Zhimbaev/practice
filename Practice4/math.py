from math import radians, tan, pi


# Convert degree to radian
degree = 15
radian = radians(degree)
print(f"Degree: {degree}")
print(f"Radian: {radian:.6f}\n")


# Calculate the area of a trapezoid
height = 5
base1 = 5
base2 = 6
trapezoid_area = (base1 + base2) * height / 2
print(f"Trapezoid area with bases {base1}, {base2} and height {height}: {trapezoid_area}\n")


# Calculate the area of a regular polygon
num_sides = 4
side_length = 25
polygon_area = (num_sides * side_length ** 2) / (4 * tan(pi / num_sides))
print(f"Regular polygon with {num_sides} sides of length {side_length}: Area = {polygon_area}\n")


# Calculate the area of a parallelogram
base = 5
height_parallelogram = 6
parallelogram_area = base * height_parallelogram
print(f"Parallelogram area with base {base} and height {height_parallelogram}: {parallelogram_area}")