import heapq
import sys

# 입력 속도 향상
input = sys.stdin.readline

def solve():
    C, N = map(int, input().split())
    
    # 빨간 돌 입력 및 정렬
    T = [int(input()) for _ in range(C)]
    T.sort()
    
    # 검은 돌 입력 및 A 기준 정렬
    AB = []
    for _ in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort()  # A[0] 기준 오름차순 정렬

    ans = 0
    active_candidates = [] # B_j 값을 담을 최소 힙
    stone_idx = 0
    
    for t in T:
        # 1. 현재 빨간 돌 t보다 시작점(A)이 작거나 같은 검은 돌을 모두 후보 힙에 추가
        while stone_idx < N and AB[stone_idx][0] <= t:
            heapq.heappush(active_candidates, AB[stone_idx][1])
            stone_idx += 1
        
        # 2. 후보들 중 끝점(B)이 현재 t보다 작은 돌은 매칭 불가능하므로 제거
        while active_candidates and active_candidates[0] < t:
            heapq.heappop(active_candidates)
            
        # 3. 유효한 후보가 있다면 가장 빨리 끝나는(B가 작은) 돌과 매칭
        if active_candidates:
            heapq.heappop(active_candidates)
            ans += 1
            
    print(ans)

solve()