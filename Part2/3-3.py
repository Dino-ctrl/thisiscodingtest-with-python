#이중 반복을 사용하지 않고 행렬을 입력받아 문제를 푸는 방법

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value) #일단 result가 선언되어 있어야 함

print(result)