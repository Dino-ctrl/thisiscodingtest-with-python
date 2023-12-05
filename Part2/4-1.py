#나는 구현이 제일 싫어
#이건 그냥 외우는게 나아

n = int(input())
x, y = 1, 1 #미리 선언
plans = input().split()

#이동 방향 만들기
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

#이동 계획을 하나씩 확인

for plan in plans:
    #이동 후 좌표 구하기
    for i in range(4): # or for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        #공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    #이동 수행
    x, y = nx, ny

print(x, y)


