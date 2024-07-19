n = int(input())
MAP = [list(map(int, input().split())) for i in range(n)]


def findMAX(x,y, MAX):
    global n
    answer = 0
    if x + 2 > n -1 or y + 2 >n - 1:
        return 0
    else:
        for i in range(3):
            for j in range(3):
               if MAP[i + x][j+ y] == 1:
                    answer += 1
        return answer
MAX = 0 
for i in range(n):
    for j in range(n):
        a = findMAX(i,j, MAX)
        if MAX < a:
            MAX = a
print(MAX)