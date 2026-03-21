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
                빙하위치.append((i, j))

    return c


dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
빙하갯수 = 빙하갯수탐색()
녹을빙하= deque()
t = 0

def 업데이트():
    while 녹을빙하:
        x,y = 녹을빙하.popleft()
        a[x][y] = 0


def 빙하기준주위물탐색():
    while 빙하위치:
        x, y = 빙하위치.popleft()
        플래그 = False
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]

            if 가능한위치(nx, ny) and a[nx][ny] == 0:
                ### 물 기준 주위 물이 있는지 확인
                for j in range(4):
                    nx2 = nx + dir[j][0]
                    ny2 = ny + dir[j][1]
                    if 가능한위치(nx2, ny2) and a[nx2][ny2] == 0:
                        플래그 = True
                        break
            if 플래그:
                녹을빙하.append((x, y))
                break
                ### 녹는 빙하란거 확인

                # 녹을빙하.append((x,y))


### 빙하의 위치를 기준으로 4방향탐색, 후보가 될 수 있는 물들 위치
### 해당 묾을 기준으로 4방 탐색 -> 만약 주위에 물이 하나도 없다면 해당 빙하는 녹음
# if 빙하갯수 == 0:
#     print(0, 0)
#

while 빙하갯수 > 0:
    t += 1
    빙하기준주위물탐색()


    업데이트()
    # print(a)
    b = 빙하갯수탐색()
    # print(녹을빙하)
    # print(b)
    if b != 0:
        빙하갯수 = b
    else:
        break
print(t, 빙하갯수)

