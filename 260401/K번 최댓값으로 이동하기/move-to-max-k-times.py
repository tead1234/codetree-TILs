n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
import heapq
from collections import deque

def vaild(x,y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False
def find_perfect_position(r,c):
    q = []
    possible = deque()
    visited = [ [0] * n  for _ in range(n)]
    # print("초기값", r, c)
    visited[r][c] = 1
    ## 탐색온료
    possible.append((r,c))
    ways = [(-1,0),(1,0),(0,-1),(0,1)]
    while possible:
        cur_x, cur_y = possible.popleft()
        for i in range(4):
            n_x = ways[i][0] + cur_x
            n_y = ways[i][1] + cur_y
            if vaild(n_x, n_y) and visited[n_x][n_y] == 0:
                if grid[n_x][n_y] < grid[cur_x][cur_y]:
                    possible.append((n_x, n_y))
                    visited[n_x][n_y] = 1
                    heapq.heappush(q,(-grid[n_x][n_y], n_x, n_y))


    if len(q) != 0:
        pw, n_x, n_y = heapq.heappop(q)
        return n_x, n_y
    else:
        return r,c
for _ in range(k):
    n_x, n_y = find_perfect_position(r-1,c-1)
    r = n_x
    c = n_y

print(r+1,c+1)
