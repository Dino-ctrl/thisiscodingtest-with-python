n, k = map(int, input().split())
cnt = 0

while True:
    # n == k로 나누어 떨어지는 수가 될 때까지 1씩 빼기
    target = (n // k) * k
    cnt += n-target
    n = target
    if n < k:
        break
    
    cnt += 1
    n //= k

#마지막으로 남은 수에 대하여 1씩 빼기
cnt += (n-1)
print(cnt)

