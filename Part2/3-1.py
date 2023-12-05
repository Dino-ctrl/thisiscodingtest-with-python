n = 1260
cnt = 0

types = [500, 100, 50, 10]


for i in types:
    cnt += n // i
    n %= i
print(cnt)

