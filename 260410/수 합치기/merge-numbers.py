n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import heapq

heapq.heapify(arr)
# print(q)
answer = 0
cnt = 0
while arr:
    if len(arr) != 0:
        f= heapq.heappop(arr)
        cnt += 1
        # answer = f
    if cnt == 1 and len(arr) != 0:
        s= heapq.heappop(arr)
        cnt = 0
    
        answer += (f + s)
        heapq.heappush(arr, f+s)
    # print(answer)

print(answer)