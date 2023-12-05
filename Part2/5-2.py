from collections import deque

#큐 구현을 위해 deque 라이브러리 사용

que = deque()

que.append(5)
que.append(2)
que.append(3)
que.append(7)
que.popleft()
que.append(1)
que.append(4)
que.popleft()

print(que)
que.reverse() #다음 출력을 위해 역순으로 바꾸기
#print(que[::-1]) 이거 안되
print(que)

# deque 라이브러리가 queue 라이브러리보다 더 간단함

