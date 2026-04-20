n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def vaild(a,b):
    if 0<= a < n and 0<= b < n:
        return True
    else:
        return False

def click(a,b):
    ways = [(-1,0), (1,0), (0, -1), (0, 1), (0,0)]
    for i in range(5):
        n_x = a + ways[i][0]
        n_y = b + ways[i][1]
        if vaild(n_x, n_y):
            if arr[n_x][n_y] == 1:
                 arr[n_x][n_y] = 0
            elif  arr[n_x][n_y] == 0:
                arr[n_x][n_y] = 1
# Please write your code here.
ans = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            if i != n -1:
                click(i+1, j)
                ans+= 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            ans = -1
            break

print(ans)
