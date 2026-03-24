n = int(input())
arr = list(input())
compare_arr = list(input())
# Please write your code here.
## 리스트 내부 값을 바꿔야 하니깐 index로 접근

def click(i):

    while i >= 0:
        if arr[i] == "G":
            arr[i] = "H"
        else:
            arr[i] = "G"
        i-=1
    # print("arr", arr)
ans =0
# print(n)
# print(arr)
for i in range(n-1, -1, -1):
    if arr[i] != compare_arr[i]:
        click(i)
        ans += 1
print(ans)

