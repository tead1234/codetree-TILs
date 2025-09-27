import sys

input = sys.stdin.readline
N = int(input())

# 입력은 (개수, 값) -> (값, 개수)로 변환 후 정렬
sortedList = sorted([tuple(map(int, input().split()))[::-1] for _ in range(N)])

# check 함수는 수정할 필요 없이 올바르게 동작합니다.
def check(n,cnt):
    global sortedList
    start = 0
    end = len(sortedList) - 1
    
    while start <= end:
        start_num = sortedList[start][0]
        end_num = sortedList[end][0]
        if start == end:
            val = sortedList[start][0]
            if val * 2 > n:
                return False
            break

        if start_num + end_num <= n:
            maked = min(cnt[start], cnt[end])
            cnt[start] -= maked
            cnt[end] -= maked
            if cnt[start] == 0:
                start += 1
            if cnt[end] == 0:
                end -= 1
        else:
            return False
    
    return True

# --- 이분 탐색 ---
가장작은c = sortedList[-1][0]
가장큰c = sortedList[-1][0] * 2
cnt = [count for value, count in sortedList]

# ★★★ 1. 정답을 저장할 변수를 추가합니다.
answer = 가장큰c 

while 가장작은c <= 가장큰c:
    c_cnt  = cnt.copy()
    mid = (가장작은c + 가장큰c) // 2
    
    result = check(mid, c_cnt)
    if result:
        # ★★★ 2. check 함수가 성공했다면, 그 mid 값이 정답 후보가 됩니다.
        answer = mid 
        가장큰c = mid - 1
    else:
        가장작은c = mid + 1

# ★★★ 3. 루프가 끝난 후, 마지막으로 성공했던 정답 후보를 출력합니다.
print(answer)