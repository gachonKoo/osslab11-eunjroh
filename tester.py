import math

def calculate_circle_properties(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return circumference, area

radius = 5.0

circumference, area = calculate_circle_properties(radius)

print(f"c = {circumference}")
print(f"area = {area}")
