n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Please write your code here.
d = {}
for i, v in enumerate(arr):
    if v in d:
        d[v] = d[v] + 1

    else:
        d[v] = 1

# print(d)

for n in nums:
    if n in d:
        print(d[n], end = " ")
    else:
        print(0, end = " ")