n, m, k = map(int, input().split())

#리스트를 전달받을 때
data = list(map(int, input().split()))
data.sort()
fisrt = data[n-1] #가장 큰 수 
second = data[n-2] #두 번째로 가장 큰 수

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += count * fisrt
result += (m-count) * second

print(result)