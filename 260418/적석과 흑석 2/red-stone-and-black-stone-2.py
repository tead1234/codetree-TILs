C, N = map(int, input().split())
T = [int(input()) for _ in range(C)]
AB = [tuple(map(int, input().split())) for _ in range(N)]
A = [ab[0] for ab in AB]
B = [ab[1] for ab in AB]

# Please write your code here.
### 아까와 같은 문제



### 빨간돌이 어떤 검은 돌들을 만족시킬 수 있는지 정리
from collections import deque
import heapq


# AB.sort(key = lambda x : (x[0],x[1]))
heapq.heapify(AB)
T.sort()


ans = 0
AB = deque(AB)
for t in T:
    # print(t)
    temp = []
    while AB:
        a,b = heapq.heappop(AB)
        # print(a,b)
        if a <= t <= b:
            # print(t)
            ans += 1
            break
        if t < a:
            temp.append((a,b))
            # heapq.heappush(AB, (a,b))
    for tem in temp:
        heapq.heappush(AB,tem)
print(ans)