n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
### x좌표기준 정ㄹㄹ

lines.sort(key= lambda x:(x[0], -x[1]))
ans = 0
겹치는리스트 = [0] * n
for i in range(n):
    flag = False
    for j in range(i+1, n):
        if i == n and j == n:
            continue
        target_line = lines[i]
        compare_line = lines[j]
        t_x, t_y = target_line
        c_x, c_y = compare_line
    ### 겹치는지 아닌지 판단하는 로직이 더필요
    ### 무조건 겹치는경우
        # if 겹치는리스트[i] ==1 or 겹치는리스트[j]==1:
        #     flag = True
        #     break
        if t_y > c_y: 
            # flag = True
            겹치는리스트[i] = 1
            겹치는리스트[j] = 1
            ### 타겟을 제외한 나머지 루프에서 제외
            # break

for i in 겹치는리스트:
    if i == 0:
        ans += 1

# if not flag:
#         ## 겹치는거 없음
#         ans += 1
#             # continue
        
print(ans)