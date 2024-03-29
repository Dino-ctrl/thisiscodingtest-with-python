#BFS : 가까운 노드부터 탐색. 선입선출 방식이 큐 자료구조 이용하는 것이 정석
#인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면 자연스럽게 먼저 들어온 것이 먼저 나가게 되어 가까운 노드부터 탐색이 진행됨

from collections import deque

#BFS 메서드 정의
def bfs(grpah, start, visited):
    # 큐 구현 위한 deque 라이브러리 사용
    que = deque([start])
    #현재 노드 방문 처리
    visited[start] = True
    #큐가 빌 때까지 반복:
    while que:
        v = que.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

bfs(graph, 1, visited)

