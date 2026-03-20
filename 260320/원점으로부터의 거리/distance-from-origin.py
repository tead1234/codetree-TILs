n = int(input())


sequence = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 절대값 함수는 abs
def 맨해튼측정(a,b):
    return abs(a- 0) + abs(b- 0)
L = []
c = 0
for s in sequence:
    # print(s)
    c += 1
    거리 = 맨해튼측정(s[0], s[1])
    # print(거리)
    L.append((s[0], s[1],c, 거리))

L.sort(key = lambda x : (x[3], x[2]))

for l in L:
    print(l[2])