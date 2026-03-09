n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
d = {}
for w in words:
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

print(max(d.values()))