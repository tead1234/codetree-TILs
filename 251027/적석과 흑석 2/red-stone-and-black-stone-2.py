import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 'sortedcontainers' 라이브러리가 필요합니다.
# 코딩 테스트 환경에서는 대부분 기본으로 설치되어 있습니다.
# 로컬에서 실행 시: pip install sortedcontainers
try:
    from sortedcontainers import SortedList
except ImportError:
    print("이 풀이를 위해서는 'sortedcontainers' 라이브러리가 필요합니다.")
    print("터미널에서 'pip install sortedcontainers'를 실행해주세요.")
    sys.exit()

# --- 입력 ---
C, N = map(int, input().split())
T = [int(input()) for _ in range(C)]
AB = [tuple(map(int, input().split())) for _ in range(N)]

# --- 알고리즘 (풀이 1) ---

# 1. 검정 돌(AB)을 끝나는 지점(B) 기준으로 오름차순 정렬합니다.
# B가 같다면 A 기준으로 오름차순 정렬 (안정성을 위해)
sorted_AB = sorted(AB, key=lambda x: (x[1], x[0]))

# 2. 빨간 돌(T)을 SortedList (멀티셋)에 저장합니다.
# SortedList는 정렬된 상태를 유지하며,
# 값 탐색(bisect)과 삭제(pop)를 모두 O(log C) 시간에 수행합니다.
red_stones = SortedList(T)

count = 0

# 3. 정렬된 검정 돌(aj, bj)을 순회합니다.
for aj, bj in sorted_AB:
    
    # 4. 이 검정 돌에 넣을 수 있는 빨간 돌을 찾습니다. (aj <= ti <= bj)
    #    그리디 전략: 조건을 만족하는 빨간 돌 중 *가장 큰* ti를 선택합니다.
    
    # 4-1. bj보다 작거나 같은(<= bj) 가장 큰 ti를 찾습니다.
    #      bisect_right(bj)는 bj보다 '초과'하는 첫 번째 값의 인덱스를 반환합니다.
    #      따라서 그 바로 앞(idx - 1)이 bj보다 작거나 같은 가장 큰 값입니다.
    idx = red_stones.bisect_right(bj)
    
    # 4-2. 만약 그런 ti가 존재한다면 (idx > 0)
    if idx > 0:
        # bj보다 작거나 같은 가장 큰 빨간 돌(ti)을 가져옵니다.
        ti = red_stones[idx - 1]
        
        # 4-3. 이 ti가 aj보다 크거나 같은지(>= aj) 확인합니다.
        if ti >= aj:
            # 5. 매칭 성공! (aj <= ti <= bj)
            count += 1
            
            # 6. 사용한 빨간 돌(ti)을 SortedList에서 제거합니다. (O(log C))
            red_stones.pop(idx - 1)

# 7. 최종 매칭 개수 출력
print(count)