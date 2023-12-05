#L자 모양으로만 움직일 수 있는 체스판에서 이동할 수 있는 경우의 수 고르기
#이동할 수 있는 경로는 [(-2, -1), (-1, -2), (1, -2), (1,2), (-1, 2), (-2,1), (2, 1), (2, -1)]

#현재 나이트 위치 입력받기
location = input()
row = int(location[1])
column = int(ord(location[0])) - int(ord('a')) + 1

#나이트가 움직일 수 있는 방향 정의 
steps = [(-2, -1), (-1, -2), (1, -2), (1,2), (-1, 2), (-2,1), (2, 1), (2, -1)]
result = 0

for step in steps:
    #이동하고자 하는 위치 확인
    n_row = row + step[0]
    n_col = column + step[1]
    #해당 위치로 이동이 가능 하다면 카운트 중가
    if n_row >= 1 and n_row <= 8 and n_col >=1 and n_col <= 8:
        result += 1

print(result)