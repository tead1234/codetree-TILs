n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
### x좌표기준 정ㄹㄹ

lines.sort(key= lambda x:(x[0], -x[1]))
ans = 0
for i in range(n-1):
    target_line = lines[i]
    compare_line = lines[i+1]
    t_x, t_y = target_line
    c_x, c_y = compare_line
    ### 겹치는지 아닌지 판단하는 로직이 더필요
    ### 무조건 겹치는경우
    if t_y > c_y:
        continue
    else:
        ans+=1
        # continue
        
print(ans)