n,m = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def findSequence(target, m):
    check = 101
    cnt = 0
    for t in target:
        if check != t:
            if m > cnt:
                check = t
                cnt = 1
            else:
                return True
        else:
            cnt += 1
    if m <= cnt:
        return True
    return False

for target in MAP:
    if findSequence(target,m):
       # print("target", target)
        answer += 1
for i in range(n):
    L = []
    for target in MAP:
        L.append(target[i])
    if findSequence(L,m):
      #
        answer += 1

print(answer)