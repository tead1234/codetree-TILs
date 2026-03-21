n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
from collections import deque
# Please write your code here.
### 물과 닿은 곳은 빙하가 녹는다
### 빙하로 둘러쌓인 물은 영향을 주지 못한다.
### 계속 해서 상태가 변하므로 계속 판단해야됨
### 마지막 다 지워지기 전 빙하 갯수를 파악해야함
###  40000 * 40000
### 물을 기준으로 생각

### 남은 얼음의 갯수를 찾는 함수
빙하위치 = deque()


def 가능한위치(a, b):
    if 0 <= a < n and 0 <= b < m:
        return True
    else:
        return False


def 빙하갯수탐색():
    c = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                c += 1
                # 빙하위치.append((i, j))

    return c


dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
# 빙하갯수 = 빙하갯수탐색()
녹을빙하= []
t = 0

def 업데이트():
    global 녹을빙하
    for 빙하 in 녹을빙하:
        a[빙하[0]][빙하[1]] = 0
    
    녹을빙하 = []

## 물인 지역부터 시작해서 탐색 
##  주위 지형이 1이면 녹을빙하에 넣어두고
### 0이면 이어서 bfs 
### 탐색이 마무리됐는데 벽에 닿지 않았다면  녹을빙하는 초기화

def 고인물탐색(x,y, visited):
    q = deque()
    q.append((x,y))
    이번탐색에서녹을빙하 = []
    visited[x][y] = 1
    Flag = False
    while q:
        cur_x, cur_y = q.popleft()
        
        if cur_x == 0 or cur_x == n-1 or cur_y == 0 or cur_y == m -1:
            Flag = True
        
        
        for i in range(4):
            nx = cur_x + dir[i][0]
            ny =  cur_y + dir[i][1]
            if 가능한위치(nx, ny):

                if visited[nx][ny] == 0 and a[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
            

                if (nx,ny) not in 이번탐색에서녹을빙하 and a[nx][ny] == 1:
                    이번탐색에서녹을빙하.append((nx,ny))

    if Flag:
        return 이번탐색에서녹을빙하
    else:
        return []

    # return True


# Flag = False
빙하갯수 = 빙하갯수탐색()
while True:
    t += 1
    visited = [[0]* m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0 and visited[i][j] == 0:
                
                탐색결과 = 고인물탐색(i,j, visited)
                녹을빙하 = list(set(녹을빙하 + 탐색결과))
                ## 리스트 끼리 합칠때 중복제거 하는 방법

    업데이트()
    c = 빙하갯수탐색()
    # print(c)
    if c == 0:
        print(t, 빙하갯수)
        break
    else:
        빙하갯수 = c
