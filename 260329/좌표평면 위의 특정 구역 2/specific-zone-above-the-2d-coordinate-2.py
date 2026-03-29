n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
# 점 들을 포함하는 가장 작은 직사각형
# 위아래로 가장 큰값 가장 작은값을 찾아서 기준으로 삼으면된다


ans = float('inf')

for p in range(n):
    ### 제외할 점의 위치
    new_x_list = x[:p] + x[p+1:]
    new_y_list = y[:p] + y[p+1:]

    
    max_x = max(new_x_list)
    max_y = max(new_y_list)
    min_x = min(new_x_list)
    min_y = min(new_y_list)

    if ans > (max_x - min_x) * (max_y - min_y):
        ans = (max_x - min_x) * (max_y - min_y)
        # print(max_x, min_x,max_y,min_y)
print(ans)