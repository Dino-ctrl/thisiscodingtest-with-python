n, k = map(int, input().split())

cnt = 0

# n이 k이상이라면 계속 나누기
while n >= k:
    #왜 while을 쓰지? 이유는 잘 모르겠지만... n이 k로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        cnt += 1
    n //= k
    cnt += 1

#마지막으로 남은 수에 대해 1씩 빼기
while n > 1:
    n -= 1
    cnt += 1

print(cnt)
