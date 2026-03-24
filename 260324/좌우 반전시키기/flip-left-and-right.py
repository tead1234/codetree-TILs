N = int(input())
a = list(map(int,input().split()))
# b = list(input())
### 중간에 리스트가 바뀌는 경우엔 어떻게 대처?
# Please write your code here.
def change(i):
    # if (i - 1) >= 0:
        # if a[i-1] ==0:
    a[i-1] = 1

    if (i + 1) < N:
        if a[i+1] ==0:
             a[i+1] = 1
        else:
            a[i+1] =0
    if a[i] == 1 :
        a[i] = 0
    else:
        a[i] = 1
    # a[i] = 1
    # print(i, a)


ind=  0
ans = 0
for i in range(1, N):
    # print(a[i])

    if  a[i-1] == 0:
        # print("진입", i)
        change(i)
        ans += 1
for i in a:
    if i == 0:
        ind = 1
# print(a)
if ind == 1:
    print(-1)
else:
    print(ans)


