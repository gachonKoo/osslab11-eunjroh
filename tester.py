import math

def calculate_circle_properties(radius):
    # 원의 둘레와 면적 계산
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return circumference, area

# 반지름 값 설정
radius = 5.0

# 계산 실행
circumference, area = calculate_circle_properties(radius)

# 출력 (Autograder가 검증할 값)
print(f"c = {circumference}")
print(f"area = {area}")
