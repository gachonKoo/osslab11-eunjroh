import math

# 반지름 값 설정
radius = 5.0

# 원의 둘레와 면적 계산
circumference = 2 * math.pi * radius  # 둘레 계산
area = math.pi * radius ** 2  # 면적 계산

# 결과 출력
print(f"c = {radius}")
print(f"area = {area}")
expected-output: |-
  c = 5.0
  area = 314.1592653589793

