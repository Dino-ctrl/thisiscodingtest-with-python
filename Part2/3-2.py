n, m, k = map(int, input().split())

#리스트를 전달받을 때
data = list(map(int, input().split()))
data.sort()
fisrt = data[n-1] #가장 큰 수 
second = data[n-2] #두 번째로 가장 큰 수

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += fisrt
        m -= 1
    if m == 0:
        break
    result += second #두 번째로 큰 수를 한 번 더하기
    m -= 1 #더할 때 마다 1씩 빼기
#이게 while 문이 트루니까 계속 반복되는 거구나. m이 0이 되서 break될 때까지

print(result)