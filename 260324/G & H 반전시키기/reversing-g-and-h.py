N = int(input())
a = list(input())
b = list(input())

# Please write your code here.

## 다른 문자열을 그룹으로 만들면 된다.
구간비교 =[]

for i in range(N):
    if a[i] != b[i]:
        구간비교.append(1)
    else:
        구간비교.append(0)

def find_group():
    구간 = False
    ans = 0
    for i in 구간비교:
        if i == 1:
            if 구간:
                continue
            else:
                구간 = True
                ans += 1
        else:
            구간 = False

    return ans
print(find_group())

