n = int(input())
arr = [input() for _ in range(n)]

# Please write your code here.
### 먼저 앞자리 수를 비교 
from functools import cmp_to_key

def compare(x,y):
    
    x_num = int(str(x) + str(y))
    y_num = int(str(y) + str(x))
    if x_num < y_num:
        return -1
    elif y_num < x_num:
        return 1
    return 0

arr.sort(key = cmp_to_key(compare), reverse = True)
answer = "".join(arr)
print(answer)

