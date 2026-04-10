n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
meetings.sort(key = lambda x : (x[1], x[0]))
last_time = -1
ans = 0
for m in meetings:
    s,e = m
    if s >= last_time:
        ans += 1
        last_time = e
print(ans)
