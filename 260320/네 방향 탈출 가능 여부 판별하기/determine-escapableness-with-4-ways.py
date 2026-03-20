n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
from collections import deque

visited = [[0] * m for _ in range(n)]
# Please write your code here.
def checkLine(a,b):
    if 0 <= a < n and 0<= b < n:
        return True
    else:
        return False
def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    dir = [(-1,0), (1,0), (0, -1), (0, 1)]
    while q:
        cur_x, cur_y = q.popleft()
        if cur_x == n-1 and cur_y == m -1:
            return True

        for i in range(4):
            d = dir[i]

            nx = d[0] + cur_x
            ny = d[1] + cur_y

            if checkLine(nx, ny) and visited[nx][ny] == False:
                ## 뱀없음
                if a[nx][ny] == 1:
                    # print(nx,ny,a[nx][ny])
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    # print(q)
    return False

if bfs():
    print(1)
else:
    print(0)